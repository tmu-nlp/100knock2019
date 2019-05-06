import sys
import re

def read_file(filename: str) -> list:
    with open(filename, "r") as file:
        cal1 = []
        cal2 = []
        for line in file: #一行ずつはいってくる
            line = line.strip('\n').split('\t') #改行を消す,タブで分割して配列に格納
            cal1.append(line[0]) #0が一列目、1が二列目
            cal2.append(line[1])

    return cal1, cal2

def write_file(filename: str, text: str):
    with open(filename, "w") as file: #wは新規作成または上書きモード
        file.write(text)

def main():
    cal1, cal2 = read_file('hightemp.txt')
    write_file('cal1.txt', '\n'.join(cal1))
    write_file('cal2.txt', '\n'.join(cal2))

if __name__ == '__main__':
    main()

#cutコマンド cut [option] file
#option  -b バイト数:切り出すバイト数を指定   -c 文字数:文字数を指定(N Nを切り出す、N- Nから行末まで、N-M NからMまで、-M 行頭からMまで)
#        -d 文字:区切り文字を指定(デフォルトはタブ)   -f 列数:切り出す列
# A :   cut -f 1 hightemp.txt > cal1_cmd.txt, cut -f 2 hightemp.txt > cal2_cmd.txt
