# 81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．

# ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
# 単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．

import random
from tqdm import tqdm


with open('./knock81.txt', 'r') as fin, \
     open('./knock82.txt', 'w+') as fo:

    for line in tqdm(fin):
        words = line.split()
        for i, t in enumerate(words):
            d = random.randrange(1, 6)    # {1,2,3,4,5}
            pre = words[max(i-d, 0):i]
            post = words[i+1: i+1+d]

            for c in pre+post:
                print(f'{t}\t{c}', file=fo)
