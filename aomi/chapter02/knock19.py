from collections import defaultdict
my_dict = defaultdict(lambda: 0)

with open('hightemp.txt', 'r') as hightemp_file:
    for line in hightemp_file:
        line = line.split('\t')
        my_dict[line[0]] += 1
my_dict = sorted(my_dict.items(), key = lambda x: -x[1])
for key, value in my_dict:
    print(str(value) + " " + key)

# cut -f 1 hightemp.txt | sort | uniq -c | sort -k 1r
