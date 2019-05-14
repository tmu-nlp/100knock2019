# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ

from knock20 import get_country_data
from knock26 import remove_emphasis_markup
import re

# 内部リンクの除去
# [[記事名]] -> 記事名
# [[記事名|表示文字]] -> 記事名|表示文字
def remove_internal_link(target: str) -> str:
    # 26 の処理 : 強調 Markup を削除したテキスト
    text = remove_emphasis_markup(target)

    pattern = r"""
        \[\[    # [[
        (.+?)   # キャプチャ対象
        \]\]    # ]]
        """
    regex = re.compile(pattern, re.MULTILINE | re.VERBOSE)
    return regex.sub(r"\1", text)


if __name__ == "__main__":
    target = get_country_data("イギリス")
    print(remove_internal_link(target))
