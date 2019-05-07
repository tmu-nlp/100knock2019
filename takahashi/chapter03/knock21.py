# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

from knock20 import get_country_data
from typing import List
import re

# '[[Category:' で始まって ']]' で終わる行をすべて取得する
def extract_category(target: str) -> List[str]:
    regex = r"^\[\[Category:.+\]\]$"
    result = re.findall(regex, target, re.MULTILINE)
    return result

if __name__ == "__main__":
    target = get_country_data("イギリス")
    for category in extract_category(target):
        print(category)