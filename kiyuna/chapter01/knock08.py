'''
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

- 英小文字ならば(219 - 文字コード)の文字に置換
- その他の文字はそのまま出力

この関数を用い，英語のメッセージを暗号化・復号化せよ．

* ROT13
https://ja.wikipedia.org/wiki/ROT13
'''


def rot13(txt: str) -> str:
    import re
    return re.sub(r'[a-z]', lambda m: chr(219 - ord(m.group(0))), txt)


def check(txt: str) -> str:
    ans = rot13(txt)
    res1 = ''.join(chr(219 - ord(c)) if 96 < ord(c) < 123 else c for c in txt)
    res2 = ''.join(chr(219 - ord(c)) if c.islower() else c for c in txt)
    assert ans == res1
    assert ans == res2


if __name__ == '__main__':
    test = 'Hello, World!　ハローワールド！'
    check(test)

    tgt = ''.join(map(chr, range(97, 123)))
    enc = rot13(tgt)
    dec = rot13(enc)
    print('暗号化:', enc)
    print('復号化:', dec)
