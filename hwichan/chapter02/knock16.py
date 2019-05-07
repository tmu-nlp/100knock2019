import sys


def read_file(filename: str) -> list:
    with open(filename, "r") as file:
        return file.readlines() #ファイルを一行ごと配列に格納,\nもついてくる


def main():
    N = int(sys.argv[1])
    l = read_file(sys.argv[2])
    split_list = [''.join(l[i : i + N]) for i in range(0, len(l), N)] #0からl配列の長さまで、Nずつ足していく
    print('\n'.join(split_list))

if  __name__  ==  '__main__':
    main()

#https://eng-entrance.com/linux-command-split
# A : split -l 行数 元ファイル名 出力ファイルベース名 (分割されたら出力ファイル+アルファベットで保存される)
