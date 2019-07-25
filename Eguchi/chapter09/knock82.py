"""
81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．
ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
"""
import random
in_f = "corpus81.100.txt"
out_f = "outpu82.100.txt"

with open(out_f, "wt", encoding="utf-8") as output_data, open(in_f, "rt", encoding="utf-8") as input_data:
    for i, line in enumerate(input_data):
        words = line.strip().split(" ")

        for j in range(len(words)):
            t = words[j]
            d = random.randint(1,5)

            for k in range(max(j-d, 0), min(j + d + 1, len(words) )):
                if j != k:
                    output = t + "\t" + words[k]
                    print('{}\t{}'.format(t, words[k]), file=output_data)
        
        if i % 100 == 0:
            print('{} done.'.format(i))

