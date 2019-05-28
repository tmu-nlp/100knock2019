import CaboCha
import pydot_ng as pydot
from knock40 import Morph
from knock41 import Chunk
from knock41 import get_chunks_list

sentence = input('文を入力してください：')

with open('sentence.cabocha', 'w', encoding='utf-8') as cabocha_file:
    c = CaboCha.Parser()
    cabocha_file.write(c.parse(
        sentence).toString(CaboCha.FORMAT_LATTICE))

edges = []
for line in get_chunks_list('sentence.cabocha'):
    for chunk in line:
        if chunk.dst != -1:
            src = chunk.surface()
            dst = line[chunk.dst].surface()
            if src != '' and dst != '':
                edges.append(((src, dst)))


graph = pydot.graph_from_edges(edges, directed=True)
graph.write_png('result.png')
