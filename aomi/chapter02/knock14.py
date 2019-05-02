N = int(input())

with open('hightemp.txt', 'r') as hightemp_file:
    cnt = 0
    for line in hightemp_file:
        if cnt >= N:
            break
        print(line, end = '')
        cnt += 1
