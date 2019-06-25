

#名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ

import CaboCha
import re
class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs



path = r"\Users\Koya\Documents\Lab\neko.txt.cabocha"
with open(path,mode = "r" ,encoding= "utf-8") as cabochaf:
    splitedlines =cabochaf.read() 
    ##print(splitedlines)
    

eachlist = []
alllist = []
for line in splitedlines.split("\n"):
    temp = line.split("\t")
    if len(temp) >= 2:
        splittemp = temp[1].split(",")
        if not splittemp[1] == "空白":
            eachlist.append(Morph(temp[0],splittemp[6],splittemp[0],splittemp[1]))
    elif temp[0] == "EOS":
        alllist.append(eachlist)
        eachlist = []


chunkeachlist =[]
chunkalllist = []
tempnum = []
srcs = [""]*1000
morphs = ""

for i, chunkline in  enumerate(splitedlines.split("\n")):
    chunktemp = chunkline.split("\t")  
    if "D" in chunkline:
        
        if len(tempnum) > 1:
            tempnum[1] = int(tempnum[1])
            tempnum[2]=int(tempnum[2].strip("D"))
            if not srcs[tempnum[2]] == "":
                srcs[tempnum[2]] = str(srcs[tempnum[2]]) + "," + str(tempnum[1])
            else:
                srcs[tempnum[2]] = tempnum[1]
            chunkeachlist.append(Chunk(morphs, tempnum[2], srcs[tempnum[1]]))
        tempnum = chunkline.split(" ")
        morphs = ""
        
    elif "EOS" in chunkline:
        
        if len(tempnum) > 1:
            tempnum[1] = int(tempnum[1])
            tempnum[2]=int(tempnum[2].strip("D"))
            if not srcs[tempnum[2]] == "":
                srcs[tempnum[2]] = str(srcs[tempnum[2]]) + "," + str(tempnum[1])
            else:
                srcs[tempnum[2]] = tempnum[1]
            chunkeachlist.append(Chunk(morphs, tempnum[2], srcs[tempnum[1]]))
        chunkalllist.append(chunkeachlist)
        chunkeachlist = []
        morphs = ""
        tempnum = []
        srcs = [""]*1000
            
    else:
        morphs = morphs + chunktemp[0] 


placeline = 7
j = placeline
#for j in range(len(chunkalllist)):
kaku = ""
for  item  in alllist[j]:
    if item.pos == "動詞":
        for chunkitem in chunkalllist[j]:
            if item.surface in chunkitem.morphs :
                numdst = int(chunkitem.dst)
                if type(chunkitem.srcs) == str:
                    numberlist = chunkitem.srcs.split(",")
                    for some_srcs in numberlist:
                        for positem in alllist[j]:
                            if positem.surface in chunkalllist[j][int(some_srcs)].morphs and positem.pos == "助詞":
                                kaku = kaku +" "+positem.surface
                    print("%s\t%s" % ( item.base, kaku))
                else:
                    for positem in alllist[j]:
                        if positem.surface in chunkalllist[j][int(chunkitem.srcs)].morphs and positem.pos == "助詞":
                            print("%s\t%s" % ( item.base, positem.surface))
