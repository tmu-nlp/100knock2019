# 70. データの入手・整形
# 文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

# 1. rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
# 2. rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
# 3. 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
# sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．

from typing import List
from random import sample


def add_label(label: str, fp: str) -> List[str]:
    return [f"{label} {l.strip()}" for l in open(fp, "r", encoding="latin-1")]


def main(path: str) -> None:
    pos = add_label("+1", path + "rt-polarity.pos")
    neg = add_label("-1", path + "rt-polarity.neg")
    data = pos + neg

    # 行をランダムに並び替え、sentiment.txt を作成する
    with open("./sentiment.txt", "w") as file:
        file.write("\n".join(sample(data, len(data))) + "\n")


if __name__ == "__main__":
    path = "../data/rt-polaritydata/"
    main(path)

"""
実行結果
$ grep "^+1" sentiment.txt | wc -l
    5331
$ grep "^-1" sentiment.txt | wc -l
    5331
"""
