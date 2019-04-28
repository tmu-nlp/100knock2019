with open("hightemp.txt", "r") as ipt:
    line_num = 0
    for i in ipt:
        line_num += 1


print(f'line_num = {line_num}')