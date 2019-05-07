'''
16. ファイルを N 分割する
自然数 N をコマンドライン引数などの手段で受け取り，入力のファイルを行単位で N 分割せよ．
同様の処理を split コマンドで実現せよ．

rm out16*
'''
from knock10 import count_lines     # -B


def split_file_in_N(fn_in, fn_out, num_div):
    total_lines = count_lines(fn_in)
    lines_per_file = (total_lines + num_div - 1) // num_div
    with open(fn_in, 'r') as f:
        for cnt in range(1, num_div + 1):
            with open(f'{fn_out}_{cnt:02d}.txt', 'w') as f_out:
                for _ in range(lines_per_file):
                    f_out.write(f.readline())
            if cnt * lines_per_file >= total_lines:
                break


if __name__ == '__main__':
    import sys

    fn_in = 'hightemp.txt'
    fn_out = 'out16'

    N = int(sys.argv[1]) if sys.argv[1:] else 2     # デフォルトは 2 分割

    split_file_in_N(fn_in, fn_out, N)


'''
def gen_lines_of_file(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            yield line


def split_file_in_N(fn_in, fn_out, num_div):
    total_lines = count_lines(fn_in)
    lines_per_file = (total_lines + num_div - 1) // num_div
    gen = gen_lines_of_file(fn_in)
    for cnt in range(1, num_div + 1):
        with open(f'{fn_out}_{cnt:02d}.txt', 'w') as f_out:
            for _ in range(lines_per_file):
                try:
                    f_out.write(gen.__next__())
                except StopIteration:
                    pass
        if cnt * lines_per_file >= total_lines:
            break
'''
