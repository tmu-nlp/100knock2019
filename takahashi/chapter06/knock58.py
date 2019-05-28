# 58. タプルの抽出
# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
# 「主語 述語 目的語」の組をタブ区切り形式で出力せよ．
# ただし，主語，述語，目的語の定義は以下を参考にせよ．
# - 述語: nsubj関係とdobj関係の子（dependant）を持つ単語
# - 主語: 述語からnsubj関係にある子（dependent）
# - 目的語: 述語からdobj関係にある子（dependent）

import xml.etree.ElementTree as ET


def main() -> None:
    tree = ET.parse("../data/nlp.txt.xml")

    for sentence in tree.iterfind("./document/sentences/sentence"):
        # 述語、主語、目的語の辞書
        predicates, subjects, objects = {}, {}, {}
        for dep in sentence.iterfind(
            "./dependencies[@type='collapsed-dependencies']/dep"
        ):
            g = dep.find("./governor")
            d = dep.find("./dependent")
            i = g.get("idx")
            dtype = dep.get("type")

            if dtype in {"nsubj", "dobj"}:
                predicates[i] = g.text
                if dtype == "nsubj":
                    subjects[i] = d.text
                else:
                    objects[i] = d.text

        for id, predicate in predicates.items():
            if (id in subjects) and (id in objects):
                print(f"{subjects[id]}\t{predicate}\t{objects[id]}")


if __name__ == "__main__":
    main()
