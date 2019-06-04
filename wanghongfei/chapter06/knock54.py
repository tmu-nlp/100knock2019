import xml.etree.ElementTree as ET

xml_tree = ET.parse("./nlp.txt.xml")
for token in xml_tree.iter("token"):
    word = token.find("word").text
    lemma = token.find("lemma").text
    pos = token.find("POS").text
    print(word, "\t", lemma, "\t", pos)