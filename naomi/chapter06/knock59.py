import xml.etree.ElementTree as ET
from collections import defaultdict


class Token:

    def __init__(self, word: str, lemma: str, pos: str, ner: str, id: int):
        # 単語
        self.word = word
        # レンマ
        self.lemma = lemma
        # 品詞
        self.pos = pos
        # ID
        self.id = int(id)
        # 固有表現
        self.ner = ner

    def print(self):
        print('{0}\t{1}\t{2}'
              .format(self.word, self.lemma, self.pos))

class Sentence:
    def __init__(self, tokens: list, id: int):
        # Tokenのリスト
        self.tokens = tokens
        # 文のID
        self.id = id

        # 文節のテキスト
        self.text = ''.join([m.word for m in self.tokens])

    def print(self):
        print(self.text)

    def get_token(self, tid: int):
        for token in self.tokens:
            if tid == token.id:
                return token
            else:
                return None


def import_sentences(path: str) -> list:

    # Sentenceオブジェクトのリスト[Chunk1, Chunk2, ....]
    sentencelist = []

    tree = ET.parse(path)
    root = tree.getroot()

    for document in root:
        for sentences in document.iter('sentences'):

            for sentence in sentences.iter('sentence'):

                # 各Sentenceについて、tokenオブジェクトを格納するリスト [token1, token2, ...]
                tokens = []

                # このSentenceのID
                sid = int(sentence.attrib['id'])

                for token in sentence.iter('token'):

                    tid = int(token.attrib['id'])
                    word = token[0].text
                    lemma = token[1].text
                    pos = token[2].text
                    ner = token[5].text

                    # Morphオブジェクトを作ってリストに追加
                    tokens.append(Token(word, lemma, pos, ner, tid))

                if tokens != []:
                    sentencelist.append(Sentence(tokens, sid))

    return sentencelist


def import_corefs(path: str) -> dict:

    # Coreference用の辞書
    # key: [sentenceid, start, end], value: representative text
    corefs = defaultdict(lambda: 0)

    tree = ET.parse(path)
    root = tree.getroot()

    for document in root:
        for coreferences in document.iter('coreference'):
            for coreference in coreferences.iter('coreference'):
                for mention in coreference.iter('mention'):

                    if mention.attrib != '':
                        reptext = mention[4].text


                    sid = int(mention[0].text)
                    start = int(mention[1].text)
                    end = int(mention[2].text)
                    # 辞書に登録
                    corefs[sid, start] = [reptext, end]
    return corefs


def main():
    inpath = 'nlp.txt.xml'
    outpath = '56.txt'
    sentences = import_sentences(inpath)
    corefs = import_corefs(inpath)

    with open(outpath, 'w+', encoding='utf-8') as fout:
        for sentence in sentences:
            for token in sentence.tokens:
                end = token.id
                reptext = ''
                tokens = []
                if (sentence.id, token.id) in corefs:
                    end, reptext = corefs[sentence.id, token.id]
                for i in range(token.id, int(end)+1):
                    if sentence.get_token(i):
                        tokens.append(sentence.get_token(i).word)
                print(' '.join(tokens))


if __name__ == '__main__':
    main()

# java -mx5g -cp "./*" 
# edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,
# lemma,ner,parse,dcoref -file nlp.txt  --add-modules java.se.ee;
