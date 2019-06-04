'''
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
'''
import sys
import xml.etree.ElementTree as ET

f_name = 'nlp.txt.xml'

tree = ET.parse(f_name)

for token in tree.iter('token'):
    word = token.find('word').text
    lemma = token.findtext('lemma')
    pos = token.findtext('POS')
    print(f'{word}\t{lemma}\t{pos}')


'''
* xml.etree.ElementTree
    - https://docs.python.org/ja/3/library/xml.etree.elementtree.html
* lemma と lexicon
    - https://ja.wikipedia.org/wiki/語彙素
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
      </sentence>
    </sentences>
  </document>
</root>
'''
