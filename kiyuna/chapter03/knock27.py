'''
27. 内部リンクの除去
26の処理に加えて，
テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ
（参考: マークアップ早見表）．
'''
# Python 3.6.2 で実行
import re
import pprint
from collections import OrderedDict
from knock25 import extract_infobox
from knock26 import remove_em


def remove_interlink(d: OrderedDict) -> OrderedDict:
    """ remove interwiki link
    [[記事名]]             => 記事名
    [[記事名|表示文字]]     => 表示文字
    [[記事名#節名|表示文字]] => 表示文字

    [[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]
    => イギリスの国章 とはしない
    """
    reg = re.compile(r'\[\[(?:[^:\]]+?\|)?([^:]+?)\]\]')
    for key, value in d.items():
        d[key] = reg.sub(r'\1', value)
    return d


if __name__ == '__main__':
    d = extract_infobox()
    d = remove_em(d)
    d = remove_interlink(d)
    pprint.pprint(d)


''' NOTE
* マークアップ早見表
-> https://ja.wikipedia.org/wiki/Help:早見表

* 特殊文字（special characters）
-> https://docs.python.org/ja/3/library/re.html#regular-expression-syntax
    * '\number':
        同じ番号のグループの中身にマッチします。グループは 1 から始まる番号をつけられます。
'''
