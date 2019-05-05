import sys
order_dic = {}
count = 0
ipt = list(sys.stdin)

for line in ipt:
    words = str(line).split("\t")
    order_dic[count] = float(words[2])
    count += 1

order_dic_sorted = sorted(order_dic.items(), key=lambda x:x[1], reverse = True)

for line in order_dic_sorted:
    print(ipt[line[0]], end = "")