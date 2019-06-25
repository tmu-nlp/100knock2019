import random
random.seed(42)

f_in_name = "knock81.txt"
f_out_name = "knock82_.txt"

cnt_w = 0
with open(f_out_name, 'w') as f_out:
    for words in map(lambda x: x.split(), open(f_in_name)):
        for i, t in enumerate(words):
            cnt_w += 1
            d = random.randrange(1, 5 + 1)
            l = words[max(i - d, 0):i]
            r = words[i + 1:i + 1 + d]
            for c in l + r:
                f_out.write(f'{t}\t{c}\n')

print(cnt_w)    # => 11878244