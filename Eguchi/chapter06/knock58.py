#Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．
# ただし，主語，述語，目的語の定義は以下を参考にせよ．
#述語: nsubj関係とdobj関係の子（dependant）を持つ単語
#主語: 述語からnsubj関係にある子（dependent）
#目的語: 述語からdobj関係にある子（dependent）

import re
import xml.etree.ElementTree as ET

path = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter06\nlp.txt"
path2 = r"C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter06\nlp.txt.xml"

def analyzer():
    tree = ET.parse(path2)
    root = tree.getroot()

    predicates = {}
    subjects = {}
    objects = {}

    for sentence in root.iterfind("./document/sentences/sentence"): 
        predicates = {}
        subjects = {}
        objects = {}       

        for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
            
            dep_type = dep.get("type") 

            if dep_type == "nsubj" or "dobj":

                governor = dep.find('./governor')
                idx = governor.get("idx")
                predicates[idx] = governor.text

                if dep_type == "nsubj":
                    subjects[idx] = dep.find('./dependent').text

                elif dep_type == "dobj":
                    objects[idx] = dep.find('./dependent').text
        
        for idx, pre in sorted(predicates.items(), key = lambda x: x[0] ):
            sub = subjects.get(idx)
            obj = objects.get(idx)
            
            if (sub != None) and (obj != None) :
                print("%s\t%s\t%s" %(sub, pre, obj))

analyzer()