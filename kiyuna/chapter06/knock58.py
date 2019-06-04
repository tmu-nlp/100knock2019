'''
58. タプルの抽出
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
「主語 述語 目的語」の組をタブ区切り形式で出力せよ．
ただし，主語，述語，目的語の定義は以下を参考にせよ．
- 述語: nsubj関係とdobj関係の子（dependant）を持つ単語
- 主語: 述語からnsubj関係にある子（dependent）
- 目的語: 述語からdobj関係にある子（dependent）
'''
import sys
import pydot
import pprint
import xml.etree.ElementTree as ET
from collections import defaultdict


class SVO:
    def __init__(self):
        self.S = self.V = self.O = None

    def __bool__(self):
        return True if self.S and self.V and self.O else False

    def __repr__(self):
        res = f'{self.S if self.S else "***"}\t'
        res += f'{self.V if self.V else "***"}\t'
        res += f'{self.O if self.O else "***"}'
        return res

    def add_edge(self, type, governor, dependent):
        if type == 'nsubj':
            self.V, self.S = governor, dependent
        if type == 'dobj':
            self.V, self.O = governor, dependent


tree = ET.parse('nlp.txt.xml')

for line in tree.iterfind('./document/sentences/sentence'):
    res = defaultdict(SVO)
    xpath = './dependencies[@type="collapsed-dependencies"]/dep'
    for dep in line.iterfind(xpath):
        if dep.get('type') in ('nsubj', 'dobj'):
            s = dep.find('governor')
            t = dep.find('dependent')
            res[int(s.get('idx'))].add_edge(dep.get('type'), s.text, t.text)
            # pprint.pprint((
            #     int(s.get('idx')),
            #     s.text, '←→'[dep.get('type') == 'dobj'], t.text
            # ), stream=sys.stderr)

    # pprint.pprint(dict(res), stream=sys.stderr)
    for svo in res.values():
        if svo:
            print(svo)


'''
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
