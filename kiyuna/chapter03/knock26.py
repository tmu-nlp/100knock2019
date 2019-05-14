'''
26. 強調マークアップの除去
25の処理時に，テンプレートの値から
MediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
（参考: マークアップ早見表）．
'''
# Python 3.6.2 で実行
import re
import pprint
from collections import OrderedDict
from knock25 import extract_infobox


def remove_em(d: OrderedDict) -> OrderedDict:
    """ remove emphasis expressions
    ''italics''
    '''bold'''
    '''''both'''''
    """
    reg = re.compile(r"'{2,}")
    for key, value in d.items():
        d[key] = reg.sub("", value)
    return d


if __name__ == '__main__':
    d = extract_infobox()
    d = remove_em(d)
    pprint.pprint(d)


''' NOTE
* マークアップ早見表
-> https://ja.wikipedia.org/wiki/Help:早見表

* 特殊文字（special characters）
-> https://docs.python.org/ja/3/library/re.html#regular-expression-syntax
    * `{m,n}`:
        直前の正規表現を m 回から n 回、
        できるだけ多く繰り返したものにマッチさせる結果の正規表現にします。
'''
