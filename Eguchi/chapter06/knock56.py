#Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．
# ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．

from pycorenlp import StanfordCoreNLP
from nltk import stem
import re
import time
import xml.etree.ElementTree as ET
from collections import defaultdict


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
        with open(path2, 'w') as f:
                f.write(output)


def analyzer(root):
        
        for coreference in root.iter('coreference') :
                mentions = coreference.findall('mention')
        mentions_dict = defaultdict()
        rep_mention = mentions[0].findtext('text')  # 代表参照表現
        mentions.remove(mentions[0])  # 参照表現のリストから代表参照表現を削除
        for mention in mentions:
                # sentence : 文番号  start : 参照表現の1単語目の番号  end : 参照表現の最終単語の番号 + 1
                mentions_dict[(int(mention.findtext('sentence')), int(mention.findtext('start')))] = \
                                (rep_mention, int(mention.findtext('end')))
        return mentions_dict
#nlp_make()

def mainone():
        tree = ET.parse(path2)
        root = tree.getroot()
        mentions_dict = analyzer(root)  # (sentence_id, token_id(start)) : (rep_mention, token_id(end))
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
        print(' '.join(token_list))

mainone()