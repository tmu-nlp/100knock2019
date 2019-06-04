from knock41 import importchunklists
import pydot


def showkakari(chunks: list):

    edges = []
    for i, chunk in enumerate(chunks):
        # 係り先がない場合は無視
        if chunk.dst == -1:
            continue
        edges.append([(i, chunk.text),
                     (chunk.dst, chunks[chunk.dst].text)])

    print(edges)
    mygraph = make_graph(edges)
    mygraph.write(path='./result.png', format='png')


def make_graph(edges: list) -> pydot.Dot:
    # edges = [((識別子１, ラベル１),(識別子２、ラベル２)), ...]

    # 有向グラフとして作成
    mydot = pydot.Dot(graph_type='digraph')

    for edge in edges:

        # ノード１
        node1 = str(edge[0][0])
        label1 = str(edge[0][1])

        # ノード２
        node2 = str(edge[1][0])
        label2 = str(edge[1][1])

        # ノードを追加
        mydot.add_node(pydot.Node(node1, label=label1))
        mydot.add_node(pydot.Node(node2, label=label2))

        # エッジ（ノード１→ノード２）を追加
        mydot.add_edge(pydot.Edge(node1, node2))

    return mydot


def main():
    path = 'neko.txt.cabocha'
    clist = importchunklists(path)

    # ３番目の文のグラフを表示
    showkakari(clist[5])


if __name__ == '__main__':
    main()
