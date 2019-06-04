import xml.etree.ElementTree as ET

xml_tree = ET.parse("./nlp.txt.xml")
for word in xml_tree.iter('word'):
    print(word.text)
