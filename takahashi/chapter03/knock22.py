# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

from knock20 import get_country_data
from knock21 import extract_category
from typing import List
import re

# [[Category:英連邦王国|*]] -> 英連邦王国
# [[Category:G8加盟国]] -> G8加盟国
def get_category_name(target: str) -> List[str]:
    matches = extract_category(target)
    result = []
    for match in matches:
        result.append(re.sub("^\[\[.+:|\|\*|]]", "", match))
    return result

if __name__ == "__main__":
    target = get_country_data("イギリス")
    for name in get_category_name(target):
        print(name)