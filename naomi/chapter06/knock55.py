import xml.etree.ElementTree as ET


class Token:

    def __init__(self, word: str, lemma: str, pos: str, ner: str, id: int):
        # 単語
        self.word = word
        # レンマ
        self.lemma = lemma
        # 品詞
        self.pos = pos
        # ID
        self.id = id
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


def main():
    inpath = 'nlp.txt.xml'
    outpath = '55.txt'
    sentences = import_sentences(inpath)

    with open(outpath, 'w+', encoding='utf-8') as fout:
        for sentence in sentences:
            for token in sentence.tokens:
                if token.ner == 'PERSON':
                    print('{0}'.format(token.word), file=fout)


if __name__ == '__main__':
    main()

# java -mx5g -cp "./*" 
# edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,
# lemma,ner,parse,dcoref -file nlp.txt  --add-modules java.se.ee;
