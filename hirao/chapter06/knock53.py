import xml.etree.ElementTree as ET

if __name__ == "__main__":
    tree = ET.parse("nlp.txt.xml")
    for word in tree.iter("word"):
        print(word.text)
