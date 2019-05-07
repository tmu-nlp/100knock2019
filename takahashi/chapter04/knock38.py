# 38. ヒストグラム
# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

from knock30 import load_morpheme_list
from knock36 import get_word_frequency

from typing import Dict, List, Tuple
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from os.path import expanduser

# 日本語フォントの読み込み
fp = FontProperties(fname = "/".join([expanduser("~"), "Library", "Fonts", "NotoSansCJKjp-DemiLight.otf"]))

def histogram(freq: Dict[str, int]) -> None:
    plt.hist(list(freq.values()), bins=20, range=(1,50))
    plt.title("ヒストグラム", fontproperties=fp)
    plt.xlabel("出現頻度", fontproperties=fp)
    plt.ylabel("単語の種類数", fontproperties=fp)
    plt.show()

if __name__ == "__main__":
    freq = get_word_frequency(load_morpheme_list())
    histogram(freq)

