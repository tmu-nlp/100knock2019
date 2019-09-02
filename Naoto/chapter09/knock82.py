'''
82. 文脈の抽出
81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．
ただし，文脈語の定義は次の通りとする．

ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
'''

import random


random.seed(0)
in_file = "out81.txt"
out_file = "out82.txt"


with open(in_file, "r") as f_in, open(out_file, "w") as f_out:
    for words in map(lambda x: x.rstrip().split(), f_in):
        for i, t in enumerate(words):
            d = random.randrange(1, 5 + 1)
            L = words[max(i - d, 0):i]
            R = words[i + 1: i + 1 + d]
            for c in L + R:
                f_out.write(f'{t}\t{c}\n')

            # con_len = random.randint(1, 5)
            # c = words[max(0, i - con_len):i].extend(words[i:min(len(words), i + con_len)])
            # print(c)
            # f_out.write(f"{t}\t{''.join(c)}\n")
