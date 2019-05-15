import xml.etree.ElementTree as ET
from collections import defaultdict
from typing import Generator, Any, Tuple, DefaultDict, List

from knock53 import load_token, Token


class Mention:
    def __init__(self,
                 sentence_id: str = None,
                 start: str = None,
                 end: str = None,
                 mention: str = None,
                 representative: bool = False,
                 representative_id: str = None) -> None:
        self.sentence_id = sentence_id
        self.start = int(start)
        self.end = int(end)
        self.text = mention
        self.representative = representative
        self.representative_id = representative_id


def load_mention(filename: str = './nlp.txt.xml') -> Generator[Mention, None, None]:
    """
    参照表現を取得
    """
    tree = ET.parse(filename)
    representative_id = -1
    for mention in tree.iter('mention'):

        if mention.attrib:
            representative_id += 1

        yield Mention(
            sentence_id=mention.find('sentence').text,
            start=mention.find('start').text,
            end=mention.find('end').text,
            mention=mention.find('text').text,
            representative=mention.attrib,
            representative_id=representative_id
        )


def make_sentence_dict(filename: str = './nlp.txt.xml') -> DefaultDict[Any, list]:
    """
    １文毎の token の辞書を作成
    """
    sentences = defaultdict(list)
    for token in load_token(filename):
        sentences[token.sentence_id].append(token)

    return sentences


def make_mention(filename: str = './nlp.txt.xml') -> Tuple[DefaultDict[Any, str], DefaultDict[Any, list]]:
    """
    参照表現，代表参照表現の辞書を作成

    Returns
    -------
    representatives = { id : representative }
    mentions_dict = { replace_len : mention }
    """
    representatives_dict = defaultdict(str)
    mentions_dict = defaultdict(list)
    for mention in load_mention(filename):
        if mention.representative:
            representatives_dict[mention.representative_id] = mention.text
        else:
            # 置換する文字列の長さ
            replace_len = int(mention.end - mention.start)
            mentions_dict[replace_len].append(mention)

    return representatives_dict, mentions_dict


def make_text(tokens: List[Token]) -> str:
    """
    token のリストから単語の文字列を作成
    """

    return ' '.join(map(lambda token: token.word, filter(lambda t: t.display, tokens)))


def main():
    # 文の辞書作成
    # sentences = { id : token_list }
    sentences = make_sentence_dict()

    # 参照表現の辞書作成
    # representatives = { id : representative }
    # mentions = { replace_len : mention }
    representatives, mentions = make_mention()

    # 置換する参照表現の単語数の少ないものから置換
    for replace_len, mention_list in sorted(mentions.items()):
        for mention in mention_list:

            # 置換する部分のみの単語を取得
            tokens = sentences[mention.sentence_id][mention.start - 1: mention.end - 1]

            # 実際に置換するのは最初の単語のみ
            token_replace = tokens[0]

            replace_text = f"{representatives[mention.representative_id]} ({make_text(tokens)})"

            # 参照表現から代表参照表現への置換
            token_replace.word = replace_text
            token_replace.representative = True

            # 実際には置換しないが，表示しない単語
            for token in tokens[1:]:
                token.display = False

    for tokens in sentences.values():
        print(f"{make_text(tokens)}")


if __name__ == '__main__':
    main()
