import xml.etree.ElementTree as ET
from nltk.tree import ParentedTree

root = ET.parse('nlp.txt.xml')

for parse in root.iterfind('.//sentences/sentence/parse'):
    tree = ParentedTree.fromstring(parse.text)
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            print(' '.join(list(subtree.leaves())))
