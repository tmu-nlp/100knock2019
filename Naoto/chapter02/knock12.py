with open("hightemp.txt", "r") as ipt, open("col1.txt", "w") as col1,\
    open("col2.txt", "w") as col2:
    for line in ipt:
        col1.write(line[0] + "\n")
        col2.write(line[1] + "\n")
