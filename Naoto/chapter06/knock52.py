'''
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ． \
    Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
'''

from stemming.porter2 import stem


def stemming(input_, output_):
    with open(input_) as f, open(output_, "w") as fw:
        for word in f:
            word = word.rstrip()
            print(stem(word), file=fw)


if __name__ == "__main__":
    input_ = "nlp_words_51.txt"
    output_ = "nlp_stemming_52.txt"
    stemming(input_, output_)