import xml.etree.ElementTree as ET
import pydot_ng as pydot


def make_graph(edges: list):
    graph = pydot.Dot(graph_type='digraph')

    for edge in edges:
        id1 = edge[0][0]
        label1 = edge[0][1]
        id2 = edge[1][0]
        label2 = edge[1][1]

        # print('{} {} {} {}\n'.format(id1, label1, id2, label2))
        # ノードの追加
        graph.add_node(pydot.Node(id1, label=label1))
        graph.add_node(pydot.Node(id2, label=label2))

        # 上で追加したノードをつなぐエッジを追加、idで判断
        graph.add_edge(pydot.Edge(id1, id2))

    return graph


def main():
    root = ET.parse('nlp2.txt.xml')

    for n, dependencies in \
            enumerate(root.iterfind('./document/sentences/sentence/dependencies[@type="collapsed-dependencies"]')):
        edges = []
        for dep in dependencies.iterfind('dep'):
            if dep.get('type') == 'punct':  # 係り元か係り先に','があったら除外、エラーが出る
                continue
            governor = dep.findall('governor')[0]  # 係り元
            dependent = dep.findall('dependent')[0]  # 係り先
            edges.append(((int(governor.get('idx')), governor.text), (int(dependent.get('idx')), dependent.text)))

        if len(edges) > 0:
            graph = make_graph(edges)
            graph.write_png('{}.png'.format(n))

        n += 1


if __name__ == '__main__':
    main()
