'''
03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving
quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から
出現順に並べたリストを作成せよ．
'''


def knock03(s: str) -> list:
    s = s.replace(',', '')
    s = s.replace('.', '')
    return [len(word) for word in s.split()]


def check03(s, ans):
    # https://docs.python.org/ja/3/library/stdtypes.html?highlight=rstrip#str.rstrip
    # >>> 'mississippi'.rstrip('ipz')
    # 'mississ'
    assert ans == [len(w.rstrip(',.')) for w in s.split()]

    import re
    # https://docs.python.org/ja/3/library/re.html?highlight=findall#regular-expression-syntax
    # https://docs.python.org/ja/3/library/re.html?highlight=findall#re.findall
    assert ans == list(map(len, re.findall(r'\w+', s)))
    # https://docs.python.org/ja/3/library/re.html?highlight=findall#re.sub
    assert ans == [*map(len, re.sub('[,|.]', '', s).split())]
    # https://docs.python.org/ja/3/library/re.html?highlight=findall#re.split
    # >>> re.split(r'(\W+)', '...words, words...')
    # ['', '...', 'words', ', ', 'words', '...', '']
    assert ans == [*map(len, re.split(r'\W+', s)[:-1])]


if __name__ == '__main__':
    s = 'Now I need a drink, alcoholic of course, '\
        'after the heavy lectures involving quantum mechanics.'

    res = knock03(s)
    print(res)

    check03(s, res)
