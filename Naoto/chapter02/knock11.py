with open("hightemp.txt", "r") as ipt, open("hightemp_out.txt", "w") as opt:
    for i in ipt:
        i = i.replace("\t", " ")
        opt.write(i)
