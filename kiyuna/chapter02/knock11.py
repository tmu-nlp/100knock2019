'''
11. タブをスペースに置換
タブ 1 文字につきスペース 1 文字に置換せよ．
確認には sed コマンド，tr コマンド，もしくは expand コマンドを用いよ．
'''


def tab2space(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            yield line.rstrip().replace('\t', ' ')


if __name__ == '__main__':
    print(*tab2space(file_name='hightemp.txt'), sep='\n')

    # for line in tab2space(file_name='hightemp.txt'): print(line)
