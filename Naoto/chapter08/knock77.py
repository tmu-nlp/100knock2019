'''
77. 正解率の計測
76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．
'''


def accuracy(path="label_add.txt"):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    with open(path, "r") as f:
        for line in f:
            ans, pre, _ = line.rstrip().split(" ")
            if ans == pre:
                if pre == "1":
                    tp += 1
                else:
                    tn += 1
            else:
                if pre == "1":
                    fp += 1
                else:
                    fn += 1
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    P = (tp) / (tp + fp)
    R = (tp) / (tp + fn)
    f1 = (2 * P * R) / (P + R)
    print(f"正解率 = {accuracy:.6}")
    print(f"適合率 = {P:.6}")
    print(f"再現率 = {R:.6}")
    print(f"F1 = {f1:.6}")


if __name__ == "__main__":
    accuracy()
