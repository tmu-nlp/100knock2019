# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

from knock10 import read_file

def sort_by_frequency(target: str) -> str:
    target = target.split("\n")
    column1 = [t.split("\t")[0] for t in target]

    dic = {}
    for c1 in column1:
        if c1 in dic:
            dic[c1] += 1
        else:
            dic[c1] = 1

    result = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    return result

if __name__ == "__main__":
    target = read_file("hightemp.txt")    
    for key, _ in sort_by_frequency(target):
        print(f"{key}")
