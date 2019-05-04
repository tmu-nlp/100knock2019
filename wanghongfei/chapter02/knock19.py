def take_second(elem):
    return elem[1]
col1 = open('./col1.txt').read().split("\n")
count = {}
for item in col1:
    count.setdefault(item,0)
    count[item] = count[item] + 1
for item,value in sorted(count.items(), key=take_second, reverse=True):
    print(item, value)