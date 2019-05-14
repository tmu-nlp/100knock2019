'''
15. 末尾のN行を出力
自然数 N をコマンドライン引数などの手段で受け取り，入力のうち末尾の N 行だけを表示せよ．
確認には tail コマンドを用いよ．
'''
import sys
stdout = sys.stdout
stderr = sys.stderr


def file_tail(file_name, N):
    '''
    Return the last n lines of a file

    See Also
    --------
    https://docs.python.org/ja/3/library/collections.html?highlight=deque#deque-recipes
    '''
    from collections import deque
    with open(file_name, 'r') as f:
        return deque(f, N)              # 常に N 個保持する


if __name__ == '__main__':
    if not sys.argv[1:]:
        stderr.write(f'Usage: {sys.argv[0]} \033[32mN\033[00m\n')
        sys.exit()

    N = int(sys.argv[1])
    fn = 'hightemp.txt'

    stdout.writelines(file_tail(fn, N))
