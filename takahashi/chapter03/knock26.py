# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ

from knock20 import get_country_data
from knock25 import extract_basic_info, extract_name_and_value
import re

# 強調マークアップの削除
# ''他との区別'' -> 他との区別
# '''''斜体と強調''''' -> 斜体と強調
def remove_emphasis(target: str) -> str:
    return re.sub("\'{2,5}", "", target)

if __name__ == "__main__":
    target = get_country_data("イギリス")
    basic_info = extract_basic_info(target)
    basic_info = remove_emphasis(basic_info)
    for name, value in extract_name_and_value(basic_info).items():
        print(f"{name}: {value}")
