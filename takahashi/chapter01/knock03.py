# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）
# 文字数を先頭から出現順に並べたリストを作成せよ．

from typing import List

def make_list_of_number_of_character(target: str) -> List[int]:
    # スペース区切りで文を分割する
    words = target.split(" ")

    # アルファベットの文字数を数える (カンマ, ドットを除く)
    # str.isalpha() : 文字列が全てアルファベットかの判定
    result = []
    for word in words:
        c = 0
        for char in word:
            if char.isalpha():
                c += 1
        result.append(c)

    return result

if __name__ == "__main__":
    target = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    print(make_list_of_number_of_character(target))