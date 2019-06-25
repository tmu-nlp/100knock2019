
with open('./chapter09/corpus.txt', 'w') as f:
    for line in open('/users/hongfeiwang/downloads/enwiki-20150112-400-r100-10576.txt', 'r'):
        tokens = []
        words = line.rstrip().split(' ')

        for word in words:
            word = word.strip('.,!?;:()[]\'"')
            if word:
                tokens.append(word)
    
        print(' '.join(tokens), file=f)
