'''
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の 1, 3, 5, 7 文字目を取り出して連結した文字列を得よ．
'''


def knock01(s: str) -> str:
    return s[::2]


if __name__ == '__main__':
    s = "パタトクカシーー"
    res = knock01(s)
    print(res)          # => パトカー
