import xml.etree.ElementTree as ET
from nltk.tree import ParentedTree

# Acknowledgements
# Thank you Yujin

root = ET.parse("nlp.txt.xml")

for s in root.iterfind("./document/sentences/sentence/parse"):
    '''
    例
    (ROOT (S (PP (NP (JJ Natural) (NN language) (NN processing)) (IN From) (NP (NNP Wikipedia))) (, ,) (NP (NP (DT the) (JJ free) (NN encyclopedia) (JJ Natural) (NN language) (NN processing)) (PRN (-LRB- -LRB-) (NP (NN NLP)) (-RRB- -RRB-))) (VP (VBZ is) (NP (NP (NP (DT a) (NN field)) (PP (IN of) (NP (NN computer) (NN science)))) (, ,) (NP (JJ artificial) (NN intelligence)) (, ,) (CC and) (NP (NP (NNS linguistics)) (VP (VBN concerned) (PP (IN with) (NP (NP (DT the) (NNS interactions)) (PP (IN between) (NP (NP (NNS computers)) (CC and) (NP (JJ human) (-LRB- -LRB-) (JJ natural) (-RRB- -RRB-) (NNS languages)))))))))) (. .))) 
    '''
    tree = ParentedTree.fromstring(s.text)
    for sub in tree.subtrees():
        if sub.label() == "NP":
            print(" ".join(list(sub.leaves())))
