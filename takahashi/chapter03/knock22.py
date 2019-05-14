# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

from knock20 import get_country_data
from typing import List
import re

# [[Category:英連邦王国|*]] -> 英連邦王国
# [[Category:G8加盟国]] -> G8加盟国
def get_category_name(target: str) -> List[str]:
    pattern = r"""
        ^               # 先頭
        \[\[Category:   # [[Category:
        (               # キャプチャ開始
            .+?         # 任意の 1 文字以上に最短一致
        )               # キャプチャ終了
        (?:             # グループ化
            \|.*        # | で始まる任意の 0 文字以上
        )?              # グループ化した文字列に 0/1 回の一致
        \]\]            # ]]
        $               # 末尾
        """
    regex = re.compile(pattern, re.MULTILINE + re.VERBOSE)
    return regex.findall(target)


if __name__ == "__main__":
    target = get_country_data("イギリス")
    for name in get_category_name(target):
        print(name)
