family_data = open("/users/hongfeiwang/downloads/questions-words.txt", "r").readlines()
flag = False
lines = []
for line in family_data:
    if line.strip() == ": family":
        flag = True
        continue
    if flag != True:
        continue
    if line.startswith(': '):
        break
    lines.append(line)
with open("./chapter10/family.txt", 'w') as f:
    f.writelines(lines)

