'''
59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．
入れ子になっている名詞句もすべて表示すること．
'''
import re
import xml.etree.ElementTree as ET
from collections import defaultdict


def term2dict(S):
    if isinstance(S[1], str):
        return {S[0]: S[1]}
    else:
        return {S[0]: tuple(map(term2dict, S[1:]))}


def append_phrases(S) -> None:
    k, *_ = S.keys()            # S は key を 1 つしか持っていない
    if isinstance(S[k], str):
        res[k].append(S[k])
        return S[k]
    else:
        phrase = ' '.join(map(append_phrases, S[k]))
        res[k].append(phrase)
        return phrase


xpath = './document/sentences/sentence/parse'
for parse in ET.parse('nlp.txt.xml').iterfind(xpath):
    S = ' ' + parse.text.rstrip()                    # 末尾の空白の脱離
    S = S.replace(',', '#') + ','                    # 文字列 ',' を保護
    S = S.replace(' (', ',@("').replace(' ', ', "')  # 空白を保護 + [",] を付加
    S = re.sub(r'(\)*,)', r'"\1', S)                 # `)` の前に `"` を付加
    S = S.replace('@', ' ').replace('#', ',')        # 脱保護
    S_parsed = eval(S[3:-1])                         # `", ` と `,` の脱離

    res = defaultdict(list)                 # グローバル変数
    append_phrases(term2dict(S_parsed))     # res に名詞句などを詰める関数

    for term in res['NP']:
        print(term)


'''
* nlp.txt.xml の構造（一部）
<root>
  <document>
    <sentences>
      <sentence id="1">
        <parse>(ROOT (S (PP (NP (JJ Natural) (NN language) (NN processing)) (IN From) (NP (NNP Wikipedia))) (, ,) (NP (NP (DT the) (JJ free) (NN encyclopedia) (JJ Natural) (NN language) (NN processing)) (PRN (-LRB- -LRB-) (NP (NN NLP)) (-RRB- -RRB-))) (VP (VBZ is) (NP (NP (NP (DT a) (NN field)) (PP (IN of) (NP (NN computer) (NN science)))) (, ,) (NP (JJ artificial) (NN intelligence)) (, ,) (CC and) (NP (NP (NNS linguistics)) (VP (VBN concerned) (PP (IN with) (NP (NP (DT the) (NNS interactions)) (PP (IN between) (NP (NP (NNS computers)) (CC and) (NP (JJ human) (-LRB- -LRB-) (JJ natural) (-RRB- -RRB-) (NNS languages)))))))))) (. .))) </parse>
      </sentence>
    </sentences>
  </document>
</root>
'''

''' 実行例
[+] parse.text

(ROOT (S (PP (IN During) (NP (DT this) (NN time))) (, ,) (NP (JJ many)
(NNS chatterbots)) (VP (VBD were) (VP (VBN written) (PP (VBG including)
(NP (NNP PARRY) (, ,) (NNP Racter) (, ,) (CC and) (NNP Jabberwacky))))) (. .)))


[+] S[3:-1]

("ROOT", ("S", ("PP", ("IN", "During"), ("NP", ("DT", "this"), ("NN", "time"))),
 (",", ","), ("NP", ("JJ", "many"), ("NNS", "chatterbots")),
 ("VP", ("VBD", "were"), ("VP", ("VBN", "written"), ("PP", ("VBG", "including"),
 ("NP", ("NNP", "PARRY"), (",", ","), ("NNP", "Racter"), (",", ","),
 ("CC", "and"), ("NNP", "Jabberwacky"))))), (".", ".")))


[+] S_parsed = eval(S[3:-1])

('ROOT',
 ('S',
  ('PP', ('IN', 'During'), ('NP', ('DT', 'this'), ('NN', 'time'))),
  (',', ','),
  ('NP', ('JJ', 'many'), ('NNS', 'chatterbots')),
  ('VP',
   ('VBD', 'were'),
   ('VP',
    ('VBN', 'written'),
    ('PP',
     ('VBG', 'including'),
     ('NP',
      ('NNP', 'PARRY'),
      (',', ','),
      ('NNP', 'Racter'),
      (',', ','),
      ('CC', 'and'),
      ('NNP', 'Jabberwacky'))))),
  ('.', '.')))


[+] term2dict(S_parsed)

{'ROOT': ({'S': ({'PP': ({'IN': 'During'},
                         {'NP': ({'DT': 'this'}, {'NN': 'time'})})},
                 {',': ','},
                 {'NP': ({'JJ': 'many'}, {'NNS': 'chatterbots'})},
                 {'VP': ({'VBD': 'were'},
                         {'VP': ({'VBN': 'written'},
                                 {'PP': ({'VBG': 'including'},
                                         {'NP': ({'NNP': 'PARRY'},
                                                 {',': ','},
                                                 {'NNP': 'Racter'},
                                                 {',': ','},
                                                 {'CC': 'and'},
                                                 {'NNP': 'Jabberwacky'})})})})},
                 {'.': '.'})},)}


[+] おまけ

    S_parsed = eval(
        re.sub(r'(\)*,)', r'"\1',
               str(' ' + parse.text.rstrip().replace(',', '#') + ',')
               .replace(' (', ',@("').replace(' ', ', "'))
        .replace('@', ' ').replace('#', ',')[3:-1]
    )

'''
