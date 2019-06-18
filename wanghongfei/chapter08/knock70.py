import random

pos_file = open("/users/hongfeiwang/desktop/rt-polaritydata/rt-polarity.pos", "r", encoding="cp1252").readlines()
neg_file = open("/users/hongfeiwang/desktop/rt-polaritydata/rt-polarity.neg", "r", encoding="cp1252").readlines()
pos_list = []
neg_list = []
for line in pos_file:
    pos_list.append("+1"+" "+line)
for line in neg_file:
    neg_list.append("-1"+" "+line)
concat = pos_list + neg_list
random.shuffle(concat)
with open("./chapter08/sentiment.txt", "w") as f:
    f.writelines(concat)