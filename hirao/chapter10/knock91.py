with open("questions-words.txt") as f, open("family.txt", mode="w") as fw:
    is_family = False
    for line in f:
        line = line.rstrip()
        if line[0] == ":":
            is_family = line.split()[1] == "family"
        elif is_family:
            fw.write(line + "\n")