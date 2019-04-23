# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(target: str) -> str:
    result = ""
    characters = list(target)

    for c in characters:
        code = ord(c)
        if ord('a') <= code <= ord('z'):
            result += chr(219 - code)
        else:
            result += c

    return result

sequence = "Hello, World."
print(cipher(sequence))
print(cipher(cipher(sequence)))