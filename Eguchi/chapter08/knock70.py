#文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．
import codecs
import random
fencoding = "cp1252"
pos_path = r"C:\Users\Koya\Documents\Lab\rt-polaritydata\rt-polaritydata\rt-polarity.pos"
neg_path = r"C:\Users\Koya\Documents\Lab\rt-polaritydata\rt-polaritydata\rt-polarity.neg"
ans_path = r"C:\Users\Koya\Documents\Lab\ans.txt"
x=""

ans = []
with codecs.open(pos_path, 'r', fencoding) as f:
    for line in f:
        ans.append("+1 "+line.strip())

with codecs.open(neg_path, 'r', fencoding) as f:
    for line in f:
        ans.append("-1 "+line.strip())

random.shuffle(ans)

with codecs.open(ans_path, 'w', fencoding) as f:
    print(*ans, sep='\n', file=f)

plus = 0
minu = 0

with codecs.open(ans_path, 'r', fencoding) as f:
    for line in f:
        if line.startswith("+1"):
            plus += 1

        elif line.startswith("-1"):
            minu += 1


print("pos:%d, neg:%d" %(plus, minu))

