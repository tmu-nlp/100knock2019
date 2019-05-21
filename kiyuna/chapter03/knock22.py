'''
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
'''
import re
import pprint


def extract_patterns(pattern):
    res = []
    reg = re.compile(pattern)
    with open('wiki_UK.txt') as f:
        for line in f:
            m = reg.search(line)
            if m:
                res.append(m.group('Category_name'))
    return res


if __name__ == '__main__':
    # tgt = r'\[\[Category:(?P<Category_name>.+?)(?P<Sortkey>\|.+)??\]\]'
    # => m.group('Sortkey') = {None, |*, |くれいとふりてん}
    tgt = r'\[\[Category:(?P<Category_name>[^|]+)\|*(?P<Sortkey>.*)\]\]'
    # => m.group('Sortkey') = {'', *, くれいとふりてん}
    # tgt = r'Category:(?P<Category_name>.+?)(\||])'
    # => Category_name の抽出だけならこれでもできる
    pprint.pprint(extract_patterns(pattern=tgt))


''' NOTE
* Match.group
-> https://docs.python.org/ja/3/library/re.html#re.Match.group

* 特殊文字
-> https://docs.python.org/ja/3/library/re.html#regular-expression-syntax
    *`(?P<name>...)`
    * `*?`, `+?`, `??`:
        '*'、'+'、および '?' 修飾子は全て 貪欲 (greedy) マッチで、
        できるだけ多くのテキストにマッチします。この挙動が望ましくない時もあります。
        修飾子の後に ? を追加すると、非貪欲 (non-greedy) あるいは 最小 (minimal)
        のマッチが行われ、できるだけ 少ない 文字にマッチします。
    * `[]`:
        文字の集合を指定するのに使います。集合の中では:
            補集合 をとって範囲内にない文字にマッチできます。
            集合の最初の文字が '^' なら、集合に 含まれない 全ての文字にマッチします。
'''
