'''
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
'''
import re
import pprint


def extract_lines(pattern):
    res = []
    reg = re.compile(pattern)
    with open('wiki_UK.txt') as f:
        for line in map(lambda x: x.rstrip(), f):
            if reg.fullmatch(line):
                res.append(line)
    return res


if __name__ == '__main__':
    pprint.pprint(extract_lines(pattern=r'\[\[Category:.+\]\]'))
    # cf. pattern = r'\[\[Category:.+(\|.+)?\]\]'


''' NOTE
* ウィキペディアのスタイル
-> https://ja.wikipedia.org/wiki/Wikipedia:スタイルマニュアル

* ウィキリンク
-> https://ja.wikipedia.org/wiki/Help:リンク
    ウィキリンク（または内部リンク）は、日本語版ウィキペディア内にある別のページへリンクします。
    ウィキリンクを表記するには、リンクする先のページ名を2連の角括弧 [[ ]] で囲みます。

* ウィキペディアのカテゴリ
-> https://ja.wikipedia.org/wiki/Help:カテゴリ
    [[Category:カテゴリ名]] or [[Category:カテゴリ名|ソートキー]]

* re.compile
-> https://docs.python.org/ja/3/library/re.html?highlight=findall#re.compile
    re.compile() を使い、結果の正規表現オブジェクトを保存して再利用するほうが、
    一つのプログラムでその表現を何回も使うときに効率的です。

* re.fullmatch
-> https://docs.python.org/ja/3/library/re.html?highlight=findall#re.fullmatch

* re.findall
-> https://docs.python.org/ja/3/library/re.html?highlight=findall#re.findall

* 特殊文字
-> https://docs.python.org/ja/3/library/re.html#regular-expression-syntax
    `.`: 改行以外の任意の文字にマッチする
    `[]`: 文字の集合を指定するのに使います。
'''
