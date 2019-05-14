# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

from knock20 import get_country_data
from typing import Dict
import re


def get_template(target: str) -> Dict[str, str]:
    pattern = r"""
        ^            # 先頭
        \|           # |
        (.+?)        # キャプチャ対象 : フィールド名
        \s           # 空白
        =            # =
        \s           # 空白
        (.+?)        # キャプチャ対象 : 値
        (?=          # positive lookahead
            \n       # 改行
            (?:\||}) # キャプチャ非対象 : | または }
        )            # グループ終了
        """
    regex = re.compile(pattern, re.MULTILINE | re.DOTALL | re.VERBOSE)
    return { data[0]:data[1] for data in regex.findall(target)}


if __name__ == "__main__":
    target = get_country_data("イギリス")
    for field, value in get_template(target).items():
        print(f"{field}\t{value}")
