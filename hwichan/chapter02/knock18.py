import sys


def read_file(filename: str) -> list:
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line.split('\t'))
    return lines

#lambda 引数:処理 で無名関数を作成できる、
def main():
    sort_list = read_file(sys.argv[1])
    sort_list = sorted(sort_list, key = lambda x: x[2], reverse = True) # sorted:配列をソートする、デフォルトは昇順、keyでソートする値を指定
    sort_list = list(map(lambda x: '\t'.join(x), sort_list)) #各要素を\tでつなげる
    print(''.join(sort_list))

if  __name__  ==  '__main__':
    main()

#https://eng-entrance.com/linux-command-split
# A) sort -k 3 -r hightemp.txt
