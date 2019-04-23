# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

from knock05 import n_gram

if __name__ == "__main__":
    target1 = "paraparaparadise"
    target2 = "paragraph"

    # n_gram 関数はリストで返されるので、集合演算を行うために set 型にキャスト
    x = set(n_gram(target1, 2))
    y = set(n_gram(target2, 2))

    print(f"X : {x}")
    print(f"Y : {y}")

    print(f"union           : {x | y}")
    print(f"intersection    : {x & y}")
    print(f"difference(X-Y) : {x - y}")
    print(f"difference(Y-X) : {y - x}")

    print(f"'se' in X? : {'se' in x}")
    print(f"'se' in Y? : {'se' in y}")