import xml.etree.ElementTree as ET
from collections import defaultdict

root = ET.parse("nlp.txt.xml")

for sentence in root.iterfind("./document/sentences/sentence"):
    sentence_id = int(sentence.get('id'))
    pp = {}
    # あとでNoneと比較するためにdictにする
    nsubj = defaultdict(lambda: None)
    dobj = defaultdict(lambda: None)
    for dep in sentence.iterfind("./dependencies[@type='collapsed-dependencies']/dep"):
        # 係り形式
        dep_type = dep.get('type')
        # 係り元
        govr = dep.find("./governor")
        # 述語のindex
        index = govr.get('idx')
        if dep_type == "nsubj":
            nsubj[index] = dep.find("./dependent").text
        elif dep_type == "dobj":
            dobj[index] = dep.find("./dependent").text
        else:
            continue
        # nsubjかdobjがあるもの(述語)のみ保存
        pp[index] = govr.text

    for index in pp.keys():
        # 述語の中で、主語と目的語があるもののみ出力
        if nsubj[index] != None and dobj[index] != None:
            print(f"{nsubj[index]}\t{pp[index]}\t{dobj[index]}")
