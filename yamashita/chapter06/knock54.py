import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')
for token in tree.iter('token'):
    word = token.find('word')
    lemma = token.find('lemma')
    pos = token.find('POS')
    print(f'{word.text}\t{lemma.text}\t{pos.text}')
