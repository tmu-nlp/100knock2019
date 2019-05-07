# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ

from knock20 import get_country_data
from knock25 import extract_basic_info, extract_name_and_value
from knock26 import remove_emphasis
import re

# 内部リンクの除去
# [[記事名]] -> 記事名
# [[記事名|表示文字]] -> 記事名|表示文字
def remove_internal_link(target: str) -> str:
    return re.sub(r'\[\[(.+?)\]\]', r'\1', target)

if __name__ == "__main__":
    target = get_country_data("イギリス")
    basic_info = extract_basic_info(target)
    basic_info = remove_emphasis(basic_info)
    basic_info = remove_internal_link(basic_info)
    for name, value in extract_name_and_value(basic_info).items():
        print(f"{name}: {value}")
