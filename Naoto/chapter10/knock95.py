'''
95. WordSimilarity-353での評価
94で作ったデータを用い，各モデルが出力する類似度のランキングと，
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
'''


def spearman(data, rank1, rank2):
    """ スピアマンの順位相関係数 ρ
    ρ = 1 - (6 Σ D^2) / (N^3 - N)
    D := 対応する X と Y の値の順位の差
    N := 値のペアの数
    """
    sigma = sum((rank1[t] - rank2[t]) ** 2 for t in data)
    N = len(data)
    return 1 - (6 * sigma) / (N**3 - N)


def solve(in_path):
    data = []
    skip = True
    for line in open(in_path):
        if skip:
            skip = False
            continue
        _, _, score1, score2 = line.split()
        data.append((float(score1), float(score2)))
    data.sort(key=lambda x: x[0], reverse=True)
    rank1 = {t: i for i, t in enumerate(data, start=1)}
    data.sort(key=lambda x: x[1], reverse=True)
    rank2 = {t: i for i, t in enumerate(data, start=1)} 
    return spearman(data, rank1, rank2)


if __name__ == '__main__':
    print(solve('out94_ch09.txt'))
    print(solve('out94_ch10.txt'))
