import itertools
import xml.etree.ElementTree as ET
# java -cp "/usr/local/lib/stanford-corenlp-full-2014-08-27/*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP
# -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file nlp.txt
from typing import Generator


class Token:
    def __init__(self,
                 sentence_id: int = None,
                 token_id: int = None,
                 word: str = None,
                 lemma: str = None,
                 pos: str = None,
                 ner: str = None,
                 display: bool = True):
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
            yield Token(sentence_id=int(sentence.attrib['id']),
                        token_id=int(token.attrib['id']),
                        word=token.find('word').text,
                        lemma=token.find('lemma').text,
                        pos=token.find('POS').text,
                        ner=token.find('NER').text)


def main(stop):
    for token in itertools.islice(load_token(), stop):
        print(token.word)


if __name__ == '__main__':
    main(50)
