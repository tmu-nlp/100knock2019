import xml.etree.ElementTree as ET
import pydot_ng as pydot
from PIL import Image

root = ET.parse("nlp.txt.xml")


def draw_graph(output_id):
    for sentence in root.iterfind("./document/sentences/sentence"):
        sentence_id = int(sentence.get('id'))
        # 指定の分だけ出力したい
        if sentence_id != output_id:
            continue
        # 有向グラフ
        graph = pydot.Dot(graph_type='digraph')
        for dep in sentence.iterfind("./dependencies[@type='collapsed-dependencies']/dep"):
            #句読点以外
            if dep.get('type') == 'punct':
                continue
            # 係り元
            govr = dep.find('./governor')
            # 係り先
            dept = dep.find('./dependent')
            # ノードとエッジの設定
            graph.add_node(pydot.Node(govr.get('idx'), label=govr.text))
            graph.add_node(pydot.Node(dept.get('idx'), label=dept.text))
            graph.add_edge(pydot.Edge(govr.get('idx'), dept.get('idx')))
        # 画像出力
        graph.write_png(f"{output_id}.png")


out_id = 2
draw_graph(out_id)
Image.open(f"{out_id}.png")
