# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ

from knock20 import get_country_data
from knock25 import get_template
from typing import Dict
import re


# 辞書をkey と value をタブ区切りのテキストに変換する
def dict2text(target: Dict[str, str]) -> str:
    return "\n".join([f"{f}\t{v}" for f, v in target.items()])


# 強調マークアップの削除
# ''他との区別'' -> 他との区別
# '''''斜体と強調''''' -> 斜体と強調
def remove_emphasis_markup(target: str) -> str:
    text = dict2text(get_template(target))

    pattern = r"\'{2,5}"
    regex = re.compile(pattern, re.MULTILINE)

    return regex.sub("", text)


if __name__ == "__main__":
    target = get_country_data("イギリス")
    print(remove_emphasis_markup(target))
