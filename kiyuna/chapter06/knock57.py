'''
57. 係り受け解析
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を
有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
'''
import pydot
import xml.etree.ElementTree as ET
from itertools import islice

f_name = 'nlp.txt.xml'

tree = ET.parse(f_name)

for k in iter(lambda: int(input('Enter a number (0: exit) -> ')), 0):
    for line in islice(tree.iterfind('./document/sentences/sentence'), k - 1, k):
        G = pydot.Dot(graph_type='digraph')  # , rankdir='LR'
        # node
        G.add_node(pydot.Node("0", label='"0: ROOT"'))
        for tid, tkn in enumerate(line.iter('token'), start=1):
            lbl = '"' + f'{tid}: ' + tkn.find('word').text + '"'
            G.add_node(pydot.Node(str(tid), label=lbl))
        # edge
        xpath = './dependencies[@type="collapsed-dependencies"]/dep'
        for dep in line.iterfind(xpath):
            lbl = dep.get('type')
            color = 'blue' if lbl in ["nsubj", "dobj"] else 'black'
            s = dep.find('./governor').get('idx')
            t = dep.find('./dependent').get('idx')
            G.add_edge(pydot.Edge(s, t, label=f'"{lbl}"', color=color))
        G.write_png(f'out57_{k}.png')


'''
* XPath 式
- https://docs.python.org/ja/3/library/xml.etree.elementtree.html#xpath-support
    - `//`:
        現在の要素の下にある全てのレベルの全ての子要素を選択します。
        例えば、.//egg は木全体から egg 要素を選択します。
* nlp.txt.xml の構造（一部）
<root>
  <document>
    <sentences>
      <sentence id="1">
        <dependencies type="basic-dependencies">
        </dependencies>
        <dependencies type="collapsed-dependencies">
          <dep type="root">
            <governor idx="0">ROOT</governor>
            <dependent idx="18">field</dependent>
          </dep>
        </dependencies>
        <dependencies type="collapsed-ccprocessed-dependencies">
        </dependencies>
        <dependencies type="enhanced-dependencies">
        </dependencies>
        <dependencies type="enhanced-plus-plus-dependencies">
        </dependencies>
      </sentence>
    </sentences>
  </document>
</root>
'''
