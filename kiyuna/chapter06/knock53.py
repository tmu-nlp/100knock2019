'''
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
'''
import os
import subprocess
import xml.etree.ElementTree as ET

f_name = 'nlp.txt'
f_xml = 'nlp.txt.xml'

# 前半
if not os.path.exists(f_xml):
    subprocess.run(
        'java -Xmx5g -cp "./stanford-corenlp-full-2018-10-05/*"'
        ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
        ' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
        ' -file ' + f_name,  # + ' 2>out53.stderr',
        shell=True,
    )

# 後半
tree = ET.parse(f_xml)
root = tree.getroot()
for word in tree.iter('word'):
    print(word.text)


'''
* Stanford Core NLP
    - https://stanfordnlp.github.io/CoreNLP/
    - https://stanfordnlp.github.io/CoreNLP/download.html
    - https://stanfordnlp.github.io/CoreNLP/cmdline.html
* xml.etree.ElementTree
    - https://docs.python.org/ja/3/library/xml.etree.elementtree.html
* nlp.txt.xml の構造（一部）
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="CoreNLP-to-HTML.xsl" type="text/xsl"?>
<root>
  <document>
    <docId>nlp.txt</docId>
    <sentences>
      <sentence id="1">
        <tokens>
          <token id="1">
            <word>Natural</word>
            <lemma>natural</lemma>
            <CharacterOffsetBegin>0</CharacterOffsetBegin>
            <CharacterOffsetEnd>7</CharacterOffsetEnd>
            <POS>JJ</POS>
            <NER>O</NER>
            <Speaker>PER0</Speaker>
          </token>
        </tokens>
        <parse>(ROOT (S (PP (NP (JJ Natural) (NN language) (NN processing)) (IN From) (NP (NNP Wikipedia))) (, ,) (NP (NP (DT the) (JJ free) (NN encyclopedia) (JJ Natural) (NN language) (NN processing)) (PRN (-LRB- -LRB-) (NP (NN NLP)) (-RRB- -RRB-))) (VP (VBZ is) (NP (NP (NP (DT a) (NN field)) (PP (IN of) (NP (NN computer) (NN science)))) (, ,) (NP (JJ artificial) (NN intelligence)) (, ,) (CC and) (NP (NP (NNS linguistics)) (VP (VBN concerned) (PP (IN with) (NP (NP (DT the) (NNS interactions)) (PP (IN between) (NP (NP (NNS computers)) (CC and) (NP (JJ human) (-LRB- -LRB-) (JJ natural) (-RRB- -RRB-) (NNS languages)))))))))) (. .))) </parse>
        <dependencies type="basic-dependencies">
        </dependencies>
        <dependencies type="collapsed-dependencies">
          <dep type="root">
            <governor idx="0">ROOT</governor>
            <dependent idx="18">field</dependent>
          </dep>
        </dependencies>
        <dependencies type="collapsed-ccprocessed-dependencies">
        </dependencies>
        <dependencies type="enhanced-dependencies">
        </dependencies>
        <dependencies type="enhanced-plus-plus-dependencies">
        </dependencies>
      </sentence>
    </sentences>
    <coreference>
      <coreference>
        <mention representative="true">
          <sentence>1</sentence>
          <start>7</start>
          <end>16</end>
          <head>12</head>
          <text>the free encyclopedia Natural language processing -LRB- NLP -RRB-</text>
        </mention>
        <mention>
          <sentence>1</sentence>
          <start>17</start>
          <end>22</end>
          <head>18</head>
          <text>a field of computer science</text>
        </mention>
      </coreference>
    </coreference>
  </document>
</root>
'''
