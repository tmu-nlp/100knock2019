def ngram_alphab(str1, n):
    w_list = str1.strip(".").replace(',', '').replace(' ', '').split()
    ab_list = []
    for i in range(len(w_list[0])):
        ab_list.append(w_list[0][i])  # アルファベットで文字列を分解する。
    print(ab_list)
    ngram_ab_list = []
    for i in range(len(ab_list)):
        ngram_ab_list.append(ab_list[i:i+n])
    return(ngram_ab_list)


seq1 = "paraparaparadise"
seq2 = "paragraph"
x = ngram_alphab(seq1, 2)
y = ngram_alphab(seq2, 2)
print(x)
print(y)
ngram_alphab_x = []
ngram_alphab_y = []
for i in x:
    if len(i)>1:
       ngram_alphab_x.append(i[0]+i[1])
    else:
        ngram_alphab_x.append(i[0])
for i in y:
    if len(i)>1:
       ngram_alphab_y.append(i[0]+i[1])
    else:
        ngram_alphab_y.append(i[0])
# Combine two separate elements togethers: ['p','a']→'pa'.
intersec = set(ngram_alphab_x).intersection(set(ngram_alphab_y))
print(intersec)
union = set(ngram_alphab_x).union(set(ngram_alphab_y))
print(union)
differ = set(ngram_alphab_x).difference(set(ngram_alphab_y))
print(differ)
print('se' in ngram_alphab_x)
print('se' in ngram_alphab_y)



