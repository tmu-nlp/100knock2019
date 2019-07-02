from operator import itemgetter

import numpy as np


def spearman(n, sum_):
    return 1 - (6 * sum_) / float(n ** 3 - n)


def sum_diff(h, p):
    sum_ = 0
    for x, y in zip(h, p):
        sum_ += (x - y) ** 2
    return sum_


def rank(path):
    rank_ = []
    for i, line in enumerate(open(path, 'r')):
        if i == 0:
            continue
        else:
            l = []
            line = line.strip().split()
            if line[3] == 'nan':
                continue
            l.append(float(line[2]))
            l.append(float(line[3]))
            rank_.append(l)

    # 人手類似度の順位を追加
    rank_.sort(key=itemgetter(0))
    for i, r in enumerate(rank_):
        r.append(i + 1)

    # モデル類似度の順位を追加
    rank_.sort(key=itemgetter(1))
    for i, r in enumerate(rank_):
        r.append(i + 1)

    return np.array(rank_)  # [人手，モデル，人手順位，モデル順位]


def main():
    rank_pred_85 = rank('knock94_85.txt')
    rank_pred_90 = rank('knock94_90.txt')
    n = len(rank_pred_85)
    print(spearman(n, sum_diff(rank_pred_85[:, -2], rank_pred_85[:, -1])))
    n = len(rank_pred_90)
    print(spearman(n, sum_diff(rank_pred_90[:, -2], rank_pred_90[:, -1])))


if __name__ == '__main__':
    main()

# 0.30057225718420344
# 0.44321646507811097
