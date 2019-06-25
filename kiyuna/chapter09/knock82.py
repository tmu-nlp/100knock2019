'''
82. 文脈の抽出
81で作成したコーパス中に出現するすべての単語tに関して，
単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．

- ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
- 単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
'''
import sys
import random
random.seed(42)

f_in_name = "out81.txt"
f_out_name = "out82.txt"

cnt_w = 0
with open(f_out_name, 'w') as f_out:
    for words in map(lambda x: x.split(), open(f_in_name)):
        for i, t in enumerate(words):
            cnt_w += 1
            d = random.randrange(1, 5 + 1)
            l = words[max(i - d, 0):i]
            r = words[i + 1:i + 1 + d]
            for c in l + r:
                f_out.write(f'{t}\t{c}\n')

print(cnt_w)    # => 11878244
