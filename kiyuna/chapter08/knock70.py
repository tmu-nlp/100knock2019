'''
70. データの入手・整形
文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

1. rt-polarity.posの各行の先頭に"+1 "という文字列を追加する
    （極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
2. rt-polarity.negの各行の先頭に"-1 "という文字列を追加する
    （極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
3. 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える

sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．
'''
import os
import sys
import random
import tarfile


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


POS = '.pos'
NEG = '.neg'
ALL = '.all'

data = {}
with tarfile.open("rt-polaritydata.tar.gz", 'r:gz') as tar:
    for tarinfo in tar:
        root, ext = os.path.splitext(tarinfo.name)
        if ext not in (POS, NEG):                   # 拡張子で判断
            continue
        message(tarinfo.name)
        label = "+1" if ext == POS else "-1"
        with tar.extractfile(tarinfo.name) as f:
            data[ext] = [
                f"{label} {line.decode('latin-1').rstrip()}\n" for line in f]
        print(f"{ext}: {len(data[ext])}")

data[ALL] = data[POS] + data[NEG]

random.seed(123)
random.shuffle(data[ALL])

with open('./sentiment.txt', 'w') as f:
    f.writelines(data[ALL])


'''
* 「sentence polarity dataset v1.0」の取説
http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.README.1.0.txt

* tarfile モジュール
https://docs.python.org/ja/3/library/tarfile.html

* random モジュール
https://docs.python.org/ja/3/library/random.html

* コマンド
$ grep "^+1" ./sentiment.txt | wc -l
    5331
$ grep "^-1" ./sentiment.txt | wc -l
    5331
'''
