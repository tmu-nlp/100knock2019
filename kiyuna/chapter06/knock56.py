'''
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，
文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．
ただし，置換するときは，
「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
'''
import sys
import pprint
import xml.etree.ElementTree as ET
from collections import defaultdict

f_name = 'nlp.txt.xml'

tree = ET.parse(f_name)

# 1. 置換する辞書を作る
# rep_dict := (sentence_id, token_start_id) -> (token_end_id, substr, rep)
rep_dict = defaultdict(list)
for coreference in tree.iterfind('./document/coreference/coreference'):
    rep = {
        e.tag: e.text
        for e in coreference.find('./mention[@representative="true"]')
    }
    for mention in coreference.iterfind('./mention'):
        if mention.attrib:      # [@representative="true"] はパス
            continue
        sentence_id = int(mention.findtext('sentence'))
        token_start_id = int(mention.findtext('start'))
        token_end_id = int(mention.findtext('end'))
        substr = mention.findtext('text')
        rep_dict[sentence_id, token_start_id].append(
            (token_end_id, substr, rep)
        )
        sys.stderr.write(f"{substr} -> {rep['text']}\n")

# 2. 辞書に基づき置換する
# rep_dict = {(sentence_id, token_start_id): (token_end_id, substr, rep)}
res = []
for sentence in tree.iterfind('./document/sentences/sentence'):
    sentence_id = int(sentence.attrib['id'])
    is_replacing = 0    # 置換する残りの単語数
    res_sentence = []
    for token_id, token in enumerate(sentence.iterfind('./tokens/token'), 1):
        if is_replacing:
            is_replacing -= 1
            continue
        if (sentence_id, token_id) in rep_dict:
            repl_after, repl_before = [], []
            for token_end_id, substr, rep in rep_dict[sentence_id, token_id]:
                is_replacing = max(is_replacing, token_end_id - token_id)
                repl_after.append(rep['text'])
                repl_before.append(substr)
            # 出力例:
            # [My head|you](your head|your)
            # 単語数でソートして置換していくと，入れ子もできそう
            # class に display というメンバ変数を作る良さそう
            res_sentence.append(
                f"[{'|'.join(repl_after)}]({'|'.join(repl_before)})"
            )
        else:
            res_sentence.append(token.findtext('word'))
    res.append(' '.join(res_sentence) + '\n')
sys.stdout.writelines(res)


'''
* nlp.txt.xml の構造（一部）
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="CoreNLP-to-HTML.xsl" type="text/xsl"?>
<root>
  <document>
    <coreference>
      <coreference>
        <mention representative="true">
          <sentence>1</sentence>
          <start>7</start>
          <end>16</end>
          <head>12</head>
          <text>the free encyclopedia Natural language processing -LRB- NLP -RRB-</text>
        </mention>
        <mention>
          <sentence>1</sentence>
          <start>17</start>
          <end>22</end>
          <head>18</head>
          <text>a field of computer science</text>
        </mention>
      </coreference>
    </coreference>
  </document>
</root>
'''
