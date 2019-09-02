'''
80. コーパスの整形
文を単語列に変換する最も単純な方法は，空白文字で単語に区切ることである． ただ，この方法では文末のピリオドや括弧などの記号が単語に含まれてしまう． そこで，コーパスの各行のテキストを空白文字でトークンのリストに分割した後，各トークンに以下の処理を施し，単語から記号を除去せよ．

トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"
空文字列となったトークンは削除
以上の処理を適用した後，トークンをスペースで連結してファイルに保存せよ．
'''


import bz2


in_file = "enwiki-20150112-400-r100-10576.txt.bz2"
out_file = "out80.txt"

with bz2.open(in_file, "rt") as f_in, open(out_file, "w") as f_out:
    for words in map(lambda x: x.rstrip().split(), f_in):
        line = " ".join([word.strip(".,!?;:()[]'\"") for word in words])
        if line:
            f_out.write(line + "\n")
