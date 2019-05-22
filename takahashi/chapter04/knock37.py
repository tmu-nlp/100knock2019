# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

from knock30 import load_morpheme_list
from knock36 import get_word_frequency

from typing import Dict, List, Tuple, Iterable
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from os.path import expanduser

# 日本語フォントの読み込み
fp = FontProperties(
    fname="/".join([expanduser("~"), "Library", "Fonts", "NotoSansCJKjp-DemiLight.otf"])
)


def plot_word_frequency(freq: List[Tuple[str, int]], num: int) -> None:
    labels = [s[0] for s in freq[:num]]
    counts = [s[1] for s in freq[:num]]
    axis = [i for i in range(num)]

    plt.bar(axis, counts, tick_label=labels, align="center")
    plt.xticks(range(num), labels, fontproperties=fp)
    plt.title(f"頻度上位 {num} 語", fontproperties=fp)
    plt.xlabel(f"出現頻度が高い {num} 語", fontproperties=fp)
    plt.ylabel("出現頻度", fontproperties=fp)
    plt.show()


if __name__ == "__main__":
    result = get_word_frequency(load_morpheme_list())
    plot_word_frequency(result, 10)
