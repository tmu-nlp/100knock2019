import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')
for token in tree.iter('token'):
    ner = token.find('NER')
    if ner.text == 'PERSON':
        person = token.find('word')
        print(f'{person.text}')
