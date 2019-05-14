# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

from knock20 import get_country_data
from typing import List
import re


def get_category(target: str) -> List[str]:
    pattern = r"""
        ^             # 先頭
        \[\[Category: # [[Category
        .+            # 任意の文字の 1 文字以上続く
        \]\]          # ]]
        $             # 末尾
        """
    regex = re.compile(pattern, re.MULTILINE | re.VERBOSE)
    return regex.findall(target)


if __name__ == "__main__":
    target = get_country_data("イギリス")
    for category in get_category(target):
        print(category)
