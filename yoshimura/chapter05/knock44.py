'''
44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
'''
import CaboCha
import pydot_ng as pydot
from knock41 import get_chunk_list

sentence = input('文を入力してください : ')

# Cabochaで入力文を解析して結果をファイルに保存
with open('sentence.cabocha', 'w') as f:
    cabocha = CaboCha.Parser()
    f.write(cabocha.parse(sentence).toString(CaboCha.FORMAT_LATTICE))

# 係り元と係り先の文節を取得
edges = []
for chunks in get_chunk_list("sentence.cabocha"):
    for chunk in chunks:
        if chunk.dst != -1:
            src = chunk.surface()
            dst = chunks[chunk.dst].surface()
            if src != '' and dst != '':
                edges.append(((src, dst)))

# グラフを描画
graph = pydot.graph_from_edges(edges, directed=True)
graph.write_png('result.png')

# pip install pydot_ng
# brew install graphviz
# pip install graphviz