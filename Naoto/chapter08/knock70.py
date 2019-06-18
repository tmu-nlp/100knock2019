'''
70. データの入手・整形
文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．
'''

from random import shuffle


def add_label(label, path) -> []:
    return [f"{label} {line.rstrip()}" for line in open(path, "r", encoding="latin-1")]


def sentiment(pos, neg, sentiment_):
    sentiment = []
    sentiment.extend(add_label("+1", pos))
    sentiment.extend(add_label("-1", neg))
    shuffle(sentiment)
    with open(sentiment_, "w", encoding="latin-1") as f:
        f.write("\n".join(sentiment))


if __name__ == "__main__":
    pos_path = "rt-polarity.pos"
    neg_path = "rt-polarity.neg"
    out_path = "sentiment.txt"
    sentiment(pos_path, neg_path, out_path)
