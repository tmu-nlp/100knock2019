#入力文中の人名をすべて抜き出せ．


from nltk import stem
import re
import time
import xml.etree.ElementTree as ET

path = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter06\nlp.txt"
path2 = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter06\nlp.txt.xml"

def analyzer():
        tree = ET.parse(path2)
        root = tree.getroot()
        for ner, person in zip(root.iter("NER"), root.iter("word") ):
            if ner.text == "PERSON":
                print(person.text)

analyzer()