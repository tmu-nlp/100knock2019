# 39. Zipfの法則
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

from knock30 import load_morpheme_list
from knock36 import get_word_frequency

from typing import Dict, List, Tuple
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from os.path import expanduser

# 日本語フォントの読み込み
fp = FontProperties(fname = "/".join([expanduser("~"), "Library", "Fonts", "NotoSansCJKjp-DemiLight.otf"]))

def zipf(freq: Dict[str, int]) -> None:
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    freq = [v for (k,v) in freq]
    rank = range(1,len(freq)+1)

    plt.scatter(rank, freq, s=1)
    plt.title("Zipfの法則", fontproperties=fp)
    plt.xlabel("単語の出現頻度順位", fontproperties=fp)
    plt.ylabel("単語の出現頻度", fontproperties=fp)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()

if __name__ == "__main__":
    freq = get_word_frequency(load_morpheme_list())
    zipf(freq)