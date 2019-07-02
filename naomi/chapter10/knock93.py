# 93. アナロジータスクの正解率の計算
# 92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．

hit = 0
count = 0
with open('out92.txt', 'r', encoding='utf-8') as f:
    for line in f:
        _, _, _, word, predicted, _ = line.rstrip().split()
        if word == predicted:
            hit += 1
        count += 1

print(f'hit rate: {hit/count}')