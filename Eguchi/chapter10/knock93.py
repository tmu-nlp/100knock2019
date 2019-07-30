#92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．

in_f = "family_out.txt"

with open(in_f, "rt") as f:
    match = 0
    total = 0

    for line in f:
        words = line.split(" ")
        total += 1
        if words[3] == words[4]:
            match += 1

print("{}% ({}/ {})" .format(match / total * 100 , match, total))