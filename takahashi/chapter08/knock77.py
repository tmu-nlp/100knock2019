# 77. 正解率の計測
# 76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．

from typing import Dict

# 適合率, 再現率, F1 スコア, 正解率を求める
def score(filename: str) -> Dict[str, float]:
    score = dict()
    tp, tn, fp, fn = 0, 0, 0, 0
    for line in open(filename, "r", encoding="utf-8"):
        correct, predict, _ = map(float, line.split("\t"))

        if correct == predict:
            if predict == 1:
                tp += 1
            else:
                tn += 1
        else:
            if predict == 1:
                fp += 1
            else:
                fn += 1

    P, R = tp / (tp + fp), tp / (tp + fn)
    score["precision"] = P
    score["recall"] = R
    score["f1"] = 2 * P * R / (P + R)
    score["accuracy"] = (tp + tn) / (tp + tn + fp + fn)
    return score

def main() -> None:
    res = score("./results/knock76.txt")
    print(f"適合率 : {res['precision']:.6}")
    print(f"再現率 : {res['recall']:.6}")
    print(f"f1     : {res['f1']:.6}")


if __name__ == "__main__":
    main()

"""
実行結果

適合率 : 0.884455
再現率 : 0.877321
f1     : 0.880874
"""