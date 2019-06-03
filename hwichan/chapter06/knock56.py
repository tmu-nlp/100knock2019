import xml.etree.ElementTree as ET
from collections import defaultdict


def make_dict(root) -> dict:
    # root.iter() : 指定されたタグを持つノードのみに処理を絞り込む。

    mentions_dict = defaultdict()

    # tokenには ElementTree インスタンスが返される。
    for coreference in root.iter('coreference'):
        mentions = coreference.findall('mention')  # 参照表現のリスト（代表参照表現も入ってる）

        if len(mentions) == 0:  # 一番最初に空の配列ができる、それを除外
            continue
        # <mention representative="true">が代表参照表現、毎回配列の一番初めに来る
        rep_mention = mentions[0].findtext('text')  # 代表参照表現
        mentions.remove(mentions[0])  # 参照表現のリストから代表参照表現を削除
        for mention in mentions:
            # sentence : 文番号  start : 参照表現の1単語目の番号  end : 参照表現の最終単語の番号 + 1
            mentions_dict[(int(mention.findtext('sentence')), int(mention.findtext('start')))] = \
                          (rep_mention, int(mention.findtext('end')))

    return mentions_dict


def main():
    root = ET.parse('nlp2.txt.xml')
    mentions_dict = make_dict(root)  # (sentence_id, token_id(start)) : (rep_mention, token_id(end))
    for sentence_id, sentence in enumerate(root.iter('sentence'), 1):
        token_list = []  # 文の単語を格納

        for token in sentence.iter('token'):
            token_list.append(token.findtext('word'))

        for n, token in enumerate(token_list):
            if token == []:
                continue

            token_id = n + 1
            key = (sentence_id, token_id)
            if key in mentions_dict:
                # n : 参照表現の1単語目の番号 mentions_dict[key][1] : 参照表現の最終単語の番号 + 1
                mention = ' '.join(token_list[n: mentions_dict[key][1] - 1])
                del token_list[n:mentions_dict[key][1] - 1]
                token_list.insert(n, '「 {} [ {} ] 」'.format(mentions_dict[key][0], mention))

        if token_list:
            print(' '.join(token_list))


if __name__ == '__main__':
    main()
