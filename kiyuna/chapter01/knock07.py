'''
07. テンプレートによる文生成
引数 x, y, z を受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x = 12, y = "気温", z = 22.4 として，実行結果を確認せよ．
'''


def knock07(x: int, y: str, z: float) -> str:

    yield '%d時の%sは%.1f' % (x, y, z)

    yield '{}時の{}は{}'.format(x, y, z)

    yield f'{x}時の{y}は{z}'

    import string
    str = '${hour}時の${info}は${value}'
    template = string.Template(str)
    yield template.substitute(hour=x, info=y, value=z)


if __name__ == '__main__':
    x, y, z = 12, "気温", 22.4

    for res in knock07(x, y, z):
        print(res)
