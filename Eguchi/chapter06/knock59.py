#Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．

import re
import xml.etree.ElementTree as ET

path = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter06\nlp.txt"
path2 = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter06\nlp.txt.xml"

pattern = re.compile(r'''
    ^
    \(
        (.*?)
        \s
        (.*)
    \)
    $
    ''', re.VERBOSE + re.DOTALL)


def analyzer():
    tree = ET.parse(path2)
    root = tree.getroot()

    for sentence in root.iterfind("./document/sentences/sentence/parse"): 
        nplist=[]
        #print(sentence.text.strip())
        if not sentence.text.strip() == None:
            print("sen=%s" %sentence.text.strip())
            ans = recursive(sentence.text.strip(), nplist)
            print("ans=%s" %ans)


def recursive(sentence, nplist):
    match = pattern.match(sentence)
    print(match)     
    if match != None:
        tag = match.group(1)
        print("tag=%s" %tag)
        contents = match.group(2)
        words = ""
        searchNum = 0 
        wordlist = []
        for mark in contents:
            if mark == "(":
                searchNum += 1
                words += mark
            elif mark ==")":
                searchNum -= 1
                words += mark

                if searchNum == 0:
                    wordlist.append(recursive(words, nplist))
                    print("words=%s" %words)
                    print("wordlist=%s" %wordlist)
                    words = ""

            else:
                if not (searchNum == 0 and mark ==" "):
                    words += mark
        
        if words != "":
            wordlist.append(words)

        ans = " ".join(wordlist)

        if tag == "NP":
            nplist.append(ans)
        
        return ans




analyzer()