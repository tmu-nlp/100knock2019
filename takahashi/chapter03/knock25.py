# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

from knock20 import get_country_data
from typing import Dict
import re

def extract_basic_info(target: str) -> str:
    regex = r"(?<=\{\{基礎情報\s国\s).+?(?=\}\}\n)"
    return re.search(regex, target, re.DOTALL).group()

def remove_newline_from_break_tags(target: str) -> str:
    return re.sub("<br/>\n", "<br>", target)

def extract_name_and_value(target: str) -> Dict[str, str]:
    target = remove_newline_from_break_tags(target)

    regex = r"^\|(.+) = (.+)"
    matches = re.findall(regex, target, re.MULTILINE)

    result = {}
    for match in matches:
        result[match[0]] = match[1]
    return result

if __name__ == "__main__":
    target = get_country_data("イギリス")
    basic_info = extract_basic_info(target)
    for name, value in extract_name_and_value(basic_info).items():
        print(f"{name}: {value}")