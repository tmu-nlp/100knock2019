import xml.etree.ElementTree as ET

# java -cp "/usr/local/lib/stanford-corenlp-full-2014-08-27/*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP
# -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file nlp.txt
from typing import Generator


class Token:
    def __init__(self, sentence_id=None, token_id=None, word=None, lemma=None, pos=None, ner=None, display=True):
        self.sentence_id = sentence_id
        self.token_id = token_id
        self.word = word
        self.lemma = lemma
        self.pos = pos
        self.ner = ner
        self.display = display

    def is_person(self) -> bool:
        return self.ner == 'PERSON'


def load_token(filename: str = './nlp.txt.xml') -> Generator[Token, None, None]:
    """
    xml から token を読み取り token 毎のクラスを返す
    """
    tree = ET.parse(filename)
    for sentence in tree.findall('.//sentences/sentence'):
        for token in sentence.iter('token'):
            yield Token(sentence_id=sentence.attrib['id'],
                        token_id=token.attrib['id'],
                        word=token.find('word').text,
                        lemma=token.find('lemma').text,
                        pos=token.find('POS').text,
                        ner=token.find('NER').text)


if __name__ == '__main__':
    import itertools

    for token in itertools.islice(load_token(), 50):
        print(token.word)
