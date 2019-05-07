with open("hightemp.txt", mode='r') as f:
    # replaceでタブをスペースに変換
    print(f.read().replace('\t', ' '))

# cat hightemp.txt | tr '\t' ' '
