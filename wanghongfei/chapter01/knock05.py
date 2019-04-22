def ngram_word(str1, n):
    w_list = str1.strip(".").replace(',', '').split(' ')
    w_list.insert(0, '<s>') 
    w_list.append('</s>') # add the start and end symbol
    ngram_word_list = []
    for i in range(len(w_list)):
        ngram_word_list.append(w_list[i:i+n])  
    print(ngram_word_list)


def ngram_alphab(str1, n):
    w_list = str1.strip(".").replace(',', '').replace(' ', '').split()
    ab_list = []
    for i in range(len(w_list[0])):
        ab_list.append(w_list[0][i])  # アルファベットで文字列を分解する。
    print(ab_list)
    ngram_ab_list = []
    for i in range(len(ab_list)):
        ngram_ab_list.append(ab_list[i:i+n])
    print(ngram_ab_list)


seq1 = 'I am an NLPer'
gram_num = 2
ngram_word(seq1, gram_num)
ngram_alphab(seq1, gram_num)



