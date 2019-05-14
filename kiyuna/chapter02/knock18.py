'''
18. 各行を 3 コラム目の数値の降順にソート
各行を 3 コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認には sort コマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

# 罠: 入力ファイルが既に降順
'''
from operator import itemgetter as get

with open('hightemp.txt', 'r') as f:
    lines = [line.split() for line in f]
    # [x] lines.sort(key=get(2), reverse=True)    # <- 数値に変換すべき
    # [o]
    lines.sort(key=lambda x: -float(x[2]))

with open('out18', 'w') as f:
    for line in lines:
        print('\t'.join(line), file=f)
