'''
93. アナロジータスクの正解率の計算
92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．
'''


def accuracy(file_name):
    ok = 0
    ng = 0
    with open(file_name, "r") as f_in:
        for words in map(lambda x: x.rstrip().split(), f_in):
            if words[3] == words[4]:
                ok += 1
            else:
                ng += 1
        acc = ok / (ok + ng)
        print(acc)


accuracy("out92_85.txt")
accuracy("out92.txt")
