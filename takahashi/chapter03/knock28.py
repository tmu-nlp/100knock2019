# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

from knock20 import get_country_data
from knock25 import extract_basic_info, extract_name_and_value
from knock26 import remove_emphasis
from knock27 import remove_internal_link
import re

def remove_mediawiki_markup(target: str) -> str:
    return re.sub(r'<.+?>', '', target)
    
if __name__ == "__main__":
    target = get_country_data("イギリス")
    basic_info = extract_basic_info(target)
    basic_info = remove_emphasis(basic_info)
    basic_info = remove_internal_link(basic_info)
    basic_info = remove_mediawiki_markup(basic_info)
    for name, value in extract_name_and_value(basic_info).items():
        print(f"{name}: {value}")