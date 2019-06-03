import random

input_pos_path = "rt-polaritydata/rt-polaritydata/rt-polarity.pos"
input_neg_path = "rt-polaritydata/rt-polaritydata/rt-polarity.neg"
output_path = "sentiment.txt"

data = []
count_pos = 0
count_neg = 0
# ラテン文字?の認識ができないようなので、latin-1を使った
with open(input_pos_path, encoding="latin-1") as f_pos:
    for line in f_pos:
        data.append(f"+1 {line}")
        count_pos += 1
with open(input_neg_path, encoding="latin-1") as f_neg:
    for line in f_neg:
        data.append(f"-1 {line}")
        count_neg += 1
random.shuffle(data)

with open(output_path, mode="w") as f_out:
    for line in data:
        f_out.write(line.strip() + "\n")
print(f"positive sample: {count_pos}\nnegative sample: {count_neg}")