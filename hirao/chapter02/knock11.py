with open("hightemp.txt", mode='r') as f:
    print(f.read().replace('\t', ' '))

# cat hightemp.txt | tr '\t' ' '
