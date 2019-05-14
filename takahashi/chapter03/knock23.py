# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

from knock20 import get_country_data
from typing import List, Tuple
import re


def get_section_name_and_level(target: str) -> List[Tuple[int, str]]:
    pattern = r"""
        ^       # 先頭
        (={2,}) # 2 文字以上の = をキャプチャ
        (.+?)   # セクション名のキャプチャ
        \1      # 1 つ目のキャプチャに一致
        $       # 末尾
        """
    regex = re.compile(pattern, re.MULTILINE | re.VERBOSE)
    res = regex.findall(target)
    # [('==', '国名'), ('==', '歴史'), ('==', '地理'), ('===', '気候'), ...
    return [(elem[0].count("=") - 1, elem[1]) for elem in res]


if __name__ == "__main__":
    target = get_country_data("イギリス")
    for data in get_section_name_and_level(target):
        print(f"{data[0]}\t{data[1]}")
