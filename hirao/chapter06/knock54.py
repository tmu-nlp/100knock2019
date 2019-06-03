import xml.etree.ElementTree as ET

if __name__ == "__main__":
    tree = ET.parse("nlp.txt.xml")
    for i, token in enumerate(tree.iter("token")):
        print(token[0].text + "\t" + token[1].text + "\t" + token[4].text)
