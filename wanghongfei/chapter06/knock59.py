import xml.etree.ElementTree as ET
import re

xml_tree = ET.parse("./nlp.txt.xml")
np_regex = re.compile(r"^\(NP.*\)$")
for parse in xml_tree.iter("parse"):
    print(parse.text)
    