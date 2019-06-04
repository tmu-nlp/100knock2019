import xml.etree.ElementTree as ET

xml_tree = ET.parse("./nlp.txt.xml")
for token in xml_tree.iter("token"):
    ner = token.find("NER").text
    if "PERSON" == ner:
        print(token.find("word").text)