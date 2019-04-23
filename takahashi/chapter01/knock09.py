# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）
# を与え，その実行結果を確認せよ．

from random import sample

def typoglycemia(target: str) -> str:
    words = target.split(" ")

    result = []
    for word in words:
        if len(word) > 4:
            # 先頭と末尾を除き、ランダムに文字列を並び替える
            # random.sample(list, int) : ランダムされたリストの生成 (第二引数は取得したい要素数)
            mid = sample(word[1:-1], len(word)-2)
            word = word[0] + "".join(mid) + word[-1]
        result.append(word)

    return " ".join(result)

if __name__ == "__main__":
    target = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(typoglycemia(target))