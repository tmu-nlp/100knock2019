'''
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，
単語と語幹をタブ区切り形式で出力せよ．
Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
'''
import sys
from nltk.stem.porter import PorterStemmer as PS
from knock51 import nlp2word

ps = PS()
for word in nlp2word():
    stem = ps.stem(word)
    print(stem)
