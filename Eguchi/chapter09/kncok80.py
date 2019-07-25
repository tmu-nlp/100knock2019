import bz2

in_f =  "enwiki-20150112-400-r100-10576.txt.bz2"
out_f = "corpus.100.txt"
ans = list()

def read_data():
    with bz2.open(in_f, "rt", encoding="utf-8") as in_data:
        for line in  in_data:
            for word in line.split(" "):
                word = word.strip().strip(".,!?;:()[]\'\"")
                if len(word) > 0:
                    ans.append(word)
    return ans

def data_write(in_data):
    with open(out_f, "w", encoding="utf-8") as out_data:
        write_data = " ".join(in_data)
        out_data.write(write_data)


temp = read_data()
data_write(temp)