'''
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
'''
import re


def extract_sections(pattern):
    res = []
    reg = re.compile(pattern)
    with open('wiki_England.txt') as f:
        for line in f:
            m = reg.match(line)
            # m = re.search(r'^' + pattern, line)
            if m:
                # heading, level = m.group(1, 2)
                heading = m.group('Heading')
                level = len(m.group('Level')) - 1
                res.append((heading, level))
    return res


if __name__ == '__main__':
    tgt = r'(?P<Level>=+)\s*(?P<Heading>.+)\s*(?P=Level)'
    print(*extract_sections(pattern=tgt), sep='\n')


''' NOTE
* ウィキペディアのセクション
-> https://ja.wikipedia.org/wiki/Help:セクション
    [[Category:カテゴリ名]] or [[Category:カテゴリ名|ソートキー]]

* search() vs. match()
-> https://docs.python.org/ja/3/library/re.html#search-vs-match
    re.match(): 文字列の先頭でのみのマッチを確認する
    re.search(): 文字列中の位置にかかわらずマッチを確認する

* 正規表現のシンタックス
-> https://docs.python.org/ja/3/library/re.html#regular-expression-syntax
    * 特殊文字（special characters）
        *`(?P=name)`:
            名前付きグループへの後方参照
        * `^`:
            (キャレット) 文字列の先頭にマッチする
    * 特殊シーケンス（special sequences）
        * `\s`:
            Unicode 空白文字 (これは [ \t\n\r\f\v] その他多くの文字) にマッチします。
'''
