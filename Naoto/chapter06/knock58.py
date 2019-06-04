'''
58. タプルの抽出
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組を\
    タブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．

述語: nsubj関係とdobj関係の子（dependant）を持つ単語
主語: 述語からnsubj関係にある子（dependent）
目的語: 述語からdobj関係にある子（dependent）
'''

import xml.etree.ElementTree as ET


def coll(input_, output_):
    count = 0
    count2 = 0
    tree = ET.parse(input_)
    root = tree.getroot()
    with open(output_, "w") as f:
        for deps in root.iter("dependencies"):
            if deps.attrib == {'type': 'collapsed-dependencies'}:
                for dep in deps:
                    if dep.attrib["type"] == "nsubj":
                        V = dep[0].text
                        V_num = dep[0].attrib["idx"]
                        S = dep[1].text
                        S_num = dep[1].attrib["idx"]
                    elif dep.attrib["type"] == "dobj":
                        V = dep[0].text
                        V_num_2 = dep[0].attrib["idx"]
                        O = dep[1].text
                        O_num = dep[1].attrib["idx"]
                        if V_num == V_num_2:
                            print(f"{S}\t{V}\t{O}", file=f)


if __name__ == "__main__":
    input_ = "nlp.txt.xml"
    output_ = "coll_58.txt"
    coll(input_, output_)
