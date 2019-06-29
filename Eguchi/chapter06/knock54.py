#Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
from pycorenlp import StanfordCoreNLP
from nltk import stem
import re
import time
import xml.etree.ElementTree as ET

path = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter06\nlp.txt"
path2 = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter06\nlp.txt.xml"
def nlp_make():
        with open(path,mode = "r",encoding='utf-8' ) as f:
                text = f.read()
        
        nlp = StanfordCoreNLP("http://localhost:9000")
        output = nlp.annotate(text, properties={'timeout': '50000',
                'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,dcoref',
                'outputFormat': 'xml'
                })        
        print(len(output))
        with open(path2, 'w') as f:
                f.write(output)

def analyzer():
        tree = ET.parse(path2)
        root = tree.getroot()
        for i ,( word, lemma, POS) in enumerate(zip(root.iter("word"), root.iter("lemma"),root.iter("POS") ) ):
                if i == 50:
                        break
                print("%s\t%s\t%s" %(word.text, lemma.text, POS.text ))

#nlp_make()
analyzer()