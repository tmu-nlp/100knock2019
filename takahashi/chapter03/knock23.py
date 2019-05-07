# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

from knock20 import get_country_data
from typing import Dict
import re

def get_section_name_and_level(target: str) -> Dict[str, int]:
    regex = r"^=+.*=+$"
    matches = re.findall(regex, target, re.MULTILINE)
    result = {}
    for match in matches:
        level = match.count("=") // 2 - 1
        name = match.replace("=", "")
        result[name] = level
    return result

if __name__ == "__main__":
    target = get_country_data("イギリス")
    for name, level in get_section_name_and_level(target).items():
        print(f"{level}\t{name}")