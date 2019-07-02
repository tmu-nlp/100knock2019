
from graphviz import Digraph

# formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
G = Digraph(format='png')
G.attr('node', shape='circle')



# 辺の追加
G.edge("a", "b")
G.edge("b", "a")
G.edge("c", "a")

print(G)

# binary_tree.pngで保存
G.render('binary_tree')