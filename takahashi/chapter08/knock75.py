# 75. 素性の重み
# 73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．

from knock72 import deserialize


def weight_rank() -> None:
    model = deserialize("model")
    names = deserialize("names")

    # モデルの重み
    weights = model.coef_[0].tolist()
    # モデルの重みの値に名前を対応させる
    res = list(zip(weights, names))
    res.sort()

    print("\n# rank : worst 10")
    for pair in res[:10]:
        print(f"{pair[1]:<10}{pair[0]:.6f}")

    print("\n# rank : top 10")
    for pair in res[:-11:-1]:
        print(f"{pair[1]:<10} {pair[0]:.6f}")


if __name__ == "__main__":
    weight_rank()

"""
# rank : worst 10
bad       -3.714984
bore      -3.295872
dull      -3.171883
fail      -2.614839
lack      -2.586758
worst     -2.526154
neither   -2.464814
wast      -2.180590
thing     -2.157001
mediocr   -2.109745

# rank : top 10
beauti     3.039511
refresh    2.780846
perform    2.594081
enjoy      2.515075
entertain  2.387747
solid      2.371048
best       2.335639
still      2.311842
fun        2.289714
engross    2.263218
"""
