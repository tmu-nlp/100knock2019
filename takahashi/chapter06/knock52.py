# 52. ステミング
# 51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，
# 単語と語幹をタブ区切り形式で出力せよ．
# Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．

from knock51 import cut_out_words
from stemming.porter2 import stem


def stemming_words() -> None:
    for words in cut_out_words():
        for word in words:
            print(f"{word}\t{stem(word)}")
        print("")


if __name__ == "__main__":
    stemming_words()
