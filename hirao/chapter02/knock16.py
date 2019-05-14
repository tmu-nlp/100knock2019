import math
# n分割のnを入力
n = int(input())
row_count = len(open('hightemp.txt').readlines())
n_list = []

# 分割した時の最大個数
# 天井関数を使用し、全体/分割数の天井で求まる
max_num = math.ceil(row_count/n)
# 分割した時の最小個数
# こっちは床関数
min_num = math.floor(row_count/n)
# 最大個数がn個ある場合から全体の個数を引いた数が最小個数を使う個数になる
min_row = max_num*n - row_count

# 最大個数、最小個数をそれぞれの個数分リストに追加
for i in range(n - min_row):
    n_list.append(max_num)
for i in range(min_row):
    n_list.append(min_num)
# 例：n=7 [4, 4, 4, 3, 3, 3, 3]
# 例：n=6 [4, 4, 4, 4, 4, 4]
# 答えのリスト
ans_list = [[] for i in range(n)]
with open('hightemp.txt', 'r') as f:
    # n_listの値を読み込み、それが0になるまでlistにappendする
    # 0になったらlistをずらす
    k = 0
    j = n_list[k]
    for i, row in enumerate(f):
        ans_list[k].append(row.replace("\n", ""))
        j -= 1
        if j == 0 and k < n-1:
            k += 1
            j = n_list[k]

for l in ans_list:
    for row in l:
        print(row)
    print("\n")

# split -l 7 "hightemp.txt" "./result16/"
