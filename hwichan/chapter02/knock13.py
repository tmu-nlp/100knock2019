import sys
import re

def read_file(filename: str) -> list:
    with open(filename, "r") as file:
        list = []
        for line in file: #一行ずつはいってくる
            line = line.strip('\n') #改行を消す
            list.append(line)

    return list

def write_file(filename: str, text: str):
    with open(filename, "w") as file: #wは新規作成または上書きモード
        file.write(text)

def main():
    cal1 = read_file('cal1.txt')
    cal2 = read_file('cal2.txt')

    cal_list = [f'{str1}\t{str2}' for str1, str2 in zip(cal1, cal2)] #zipは要素が少ない方に合わせる
    write_file('marge.txt', '\n'.join(cal_list))

if __name__ == '__main__':
    main()

#pasteコマンド  paste [option] filename1 filename2 ...
#option     -d 結合文字:結合文字指定(デフォルトはタブ？)          -s:結合したものの行列入れ替え
# A : paste cal1.txt cal2.txt
