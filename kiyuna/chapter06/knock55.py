'''
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
'''
import sys
import xml.etree.ElementTree as ET

f_name = 'nlp.txt.xml'

tree = ET.parse(f_name)

# NER を全て抽出
print({token.text for token in tree.iter('NER')}, file=sys.stderr)

# NER="PERSON" という名前の子を持つすべての要素を選択
x_path = './document/sentences/sentence/tokens/token[NER="PERSON"]'
for token in tree.iterfind(x_path):
    print(type(token))
    print(token.find('word').text)


'''
* XPath 式
- https://docs.python.org/ja/3/library/xml.etree.elementtree.html#xpath-support
* Named Entity Recognition – NERClassifierCombiner
- https://stanfordnlp.github.io/CoreNLP/ner.html
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
