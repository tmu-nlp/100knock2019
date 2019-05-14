# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

from knock20 import get_country_data
from knock27 import remove_internal_link
import re


def remove_mediawiki_markup(target: str) -> str:
    text = remove_internal_link(target)

    # {{lang|en|United Kingdom of Great Britain and Northern Ireland}}
    #   -> United Kingdom of Great Britain and Northern Ireland
    regex_lang = re.compile(
        r"""
        \{\{lang    # {{lang
        (?:         # 非キャプチャ対象
            [^|]*?  # | 以外の文字に一致
            \|      # |
        )*?         # 非キャプチャ対象が 0 回以上
        ([^|]+?)    # | 以外の文字に一致
        \}\}        # }}
        """,
        re.MULTILINE | re.VERBOSE,
    )

    # [url: text] -> text
    regex_url = re.compile(
        r"""
        \[http://   # [http://
        (?:         # 非キャプチャ対象
            [^\s]*? # 空白以外の文字に最短一致
            \s      # 空白
        )?          # URL の内部に空白は含まれないので 1 回
        (.+?)       # キャプチャ対象 : 文字
        \]          # ]
        """,
        re.MULTILINE | re.VERBOSE,
    )

    # <ref ../>, <br/> の削除
    regex_tags = re.compile(
        r"""
        <           # <
        \/?         # / が 0or1 回
        [br|ref]    # br か ref
        [^>]*?      # > 以外の文字に一致
        >           # >
        """,
        re.MULTILINE | re.VERBOSE,
    )

    # メディアファイルの整形
    regex_file = re.compile(
        r"""
        ファイル:    # ファイル:
        ([^|]+?)    # キャプチャ対象 : ファイル名
        \|          # |
        (?:.+?)     # 末尾まで非キャプチャ
        $           # 末尾
        """,
        re.MULTILINE | re.VERBOSE,
    )

    text = regex_lang.sub(r"\1", text)
    text = regex_url.sub(r"\1", text)
    text = regex_tags.sub("", text)
    text = regex_file.sub(r"\1", text)

    return text


if __name__ == "__main__":
    target = get_country_data("イギリス")
    print(remove_mediawiki_markup(target))
