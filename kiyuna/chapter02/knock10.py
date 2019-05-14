'''
10. 行数のカウント
行数をカウントせよ．確認には wc コマンドを用いよ．
'''


def count_lines(file_name):
    with open(file_name, 'r') as f:
        # ジェネレータを使う
        # 参考: https://www.python.org/dev/peps/pep-0289/
        return sum(1 for _ in f)        # 速度とメモリ，共に良い

        # 以下の方法は，メモリに優しくない
        # return len(f.readlines())                     => 24
        # return len(f.read().rstrip().split('\n'))     => 25


if __name__ == '__main__':
    fn = 'hightemp.txt'
    print(count_lines(file_name=fn))        # => 24
