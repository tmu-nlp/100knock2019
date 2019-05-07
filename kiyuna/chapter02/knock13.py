'''
13. col1.txt と col2.txt をマージ
12 で作った col1.txt と col2.txt を結合し，
元のファイルの 1 列目と 2 列目をタブ区切りで並べたテキストファイルを作成せよ．
確認には paste コマンドを用いよ．
'''
import knock12      # col1.txt, col2.txt を作成するため, -B をつけて実行


def marge_cols(sep, *fnames):
    for cols in zip(*map(open, fnames)):
        yield sep.join(map(lambda col: col.rstrip(), cols))


if __name__ == '__main__':
    fn1 = 'col1.txt'
    fn2 = 'col2.txt'

    with open('out13', 'w') as f:
        for line in marge_cols('\t', fn1, fn2):
            f.write(line + '\n')
