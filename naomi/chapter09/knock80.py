# 80. コーパスの整形
# 文を単語列に変換する最も単純な方法は，空白文字で単語に区切ることである．ただ，この方法では文末のピリオドや括弧などの記号が単語に含まれてしまう.
# そこで，コーパスの各行のテキストを空白文字でトークンのリストに分割した後，各トークンに以下の処理を施し，単語から記号を除去せよ．

# トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"
# 空文字列となったトークンは削除
# 以上の処理を適用した後，トークンをスペースで連結してファイルに保存せよ．

import bz2
from tqdm import tqdm

path = 'enwiki-20150112-400-r10-105752.txt.bz2'
path = 'enwiki-20150112-400-r100-10576.txt.bz2'

with open('knock80 .txt', 'w+') as fo:
    for sentence in tqdm(bz2.open(path, mode='rb')):
        sentence = sentence.decode('utf-8')
        tokens = []

        for token in sentence.rstrip().split():
            token = token.strip(r'.,!?;:()[]\'\"')
            if token != '':
                tokens.append(token)
        if tokens != []:
            print(' '.join(tokens), file=fo)
