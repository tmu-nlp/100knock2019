import sys

file = open(sys.argv[1], "r")

# for文
# i = 0
# for line in file:
#     i += 1
# print(i)

#readlines() fileを一行ずつ読み込んでlistに格納
# print(file.readlines())
print(len(file.readlines()))

file.close()

# wcコマンド  wc [option] [file]
# option -c:バイト数 -m:文字数 -l:改行の数
#        -w:単語数(空白や改行文字で区切られたもの) -L:最長の行の長さ
