'''
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
'''
# Python 3.6.2 で実行
import re
import sys
import pprint
from collections import OrderedDict


def extract_infobox():
    with open('wiki_England.txt') as f:
        pattern = r'{{基礎情報[^|]+(?P<Infobox_body>.+?)}}\n'
        match = re.search(pattern, f.read(), re.DOTALL)
        info_body = match.group('Infobox_body')
        subptn = r'^\|(.+?)\s*=\s*(.+?)(?<!<br/>)\n'
        reg = re.compile(subptn, re.MULTILINE | re.DOTALL)
        od = OrderedDict(reg.findall(info_body))
        return od


if __name__ == '__main__':
    d = extract_infobox()
    pprint.pprint(d)


''' NOTE
* ウィキペディアの基礎情報_国
-> https://ja.wikipedia.org/wiki/Template:基礎情報_国

* 特殊文字（special characters）
-> https://docs.python.org/ja/3/library/re.html#regular-expression-syntax
    * `^`:
        (キャレット) 文字列の先頭にマッチし、
        MULTILINE モードでは各改行の直後にもマッチします。

* モジュールコンテンツ
-> https://docs.python.org/ja/3/library/re.html?highlight=findall#module-contents
    * re.MULTILINE / re.M / (?m)
        指定されていると、
        パターン文字 '^' は文字列の先頭で、および各行の先頭 (各改行の直後)
        パターン文字 '$' は文字列の末尾で、および各行の末尾 (各改行の直前) でマッチします。
        デフォルトでは、
        '^' は文字列の先頭でのみ、
        '$' は文字列の末尾および文字列の末尾の改行 (もしあれば) の直前でのみマッチします。
    * re.DOTALL / re.S / (?s)
        '.' 特殊文字を、改行を含むあらゆる文字にマッチさせます。
'''
