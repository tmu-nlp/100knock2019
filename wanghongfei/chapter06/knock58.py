import xml.etree.ElementTree as ET

xml_tree = ET.parse("./nlp.txt.xml")
for dependency in xml_tree.iter("dependencies"):
    if dependency.get("type") == "basic-dependencies":
        nsubj_list = []
        dobj_list = []
        for dep in dependency.iter("dep"):
            if dep.get("type") == "nsubj" :
                nsubj_dependent = dep.find("dependent").text
                nsubj_governor = dep.find("governor").text
                nsubj_list.append((nsubj_governor,nsubj_dependent))
            if dep.get("type") == "dobj":
                dobj_dependent = dep.find("dependent").text
                dobj_governor = dep.find("governor").text
                dobj_list.append((dobj_governor,dobj_dependent))
        for nsubj in nsubj_list:
            for dobj in dobj_list:
                if nsubj[0] == dobj[0]:
                    print(nsubj[1],nsubj[0],dobj[1])

