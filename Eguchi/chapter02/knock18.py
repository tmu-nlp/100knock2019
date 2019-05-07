path = r"\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter02"

with open(path + "\hightemp.txt", "r",encoding="utf-8") as file:
    readfile = file.read()
    print(readfile)
    listfile = readfile.split('\n')
    file.seek(0)
    filenumber = len(file.readlines())

splitlist= []

for i in listfile:
    splitlist.append(i.split("\t"))


splitlist.pop()
ans=[]

ans = sorted(splitlist, key=lambda x: x[2], reverse=False)

ans = list(map(lambda x: "\t".join(x), ans))
print("\n".join(ans))
