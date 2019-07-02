correct_num = 0
for index, line in enumerate(open("./chapter10/family_sim.txt", "r").readlines()):
    words = line.strip().split()
    if words[3] == words[4]:
        correct_num += 1
print(correct_num/(index+1))