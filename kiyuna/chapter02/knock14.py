'''
14. 先頭から N 行を出力
自然数 N をコマンドライン引数などの手段で受け取り，入力のうち先頭の N 行だけを表示せよ．
確認には head コマンドを用いよ．
'''
import sys
stdout = sys.stdout
stderr = sys.stderr


def file_head(file_name, N):
    with open(file_name, 'r') as f:
        for _ in range(N):
            yield f.readline()


if __name__ == '__main__':
    if not sys.argv[1:]:
        stderr.write(f'Usage: {sys.argv[0]} \033[32mN\033[00m\n')
        sys.exit()

    N = int(sys.argv[1])
    fn = 'hightemp.txt'

    for line in file_head(fn, N):
        stdout.write(line)
