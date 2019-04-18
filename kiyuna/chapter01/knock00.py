'''
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
'''


def knock00(s: str) -> str:
    return s[::-1]


if __name__ == '__main__':
    s = "stressed"
    res = knock00(s)
    print(res)          # => desserts

    # OK
    print(''.join(reversed(s)))     # return a reverse iterator
    exit()

    # NG
    s.reverse()                     # strings are immutable sequences
    print(s)
    # https://docs.python.org/ja/3/library/stdtypes.html#mutable-sequence-types
