s1 = "paraparaparadise"
s2 = "paragraph"

def n_gram(n, seq, output_type='word'):
    output = []
    if output_type == 'word':
        seq = seq.split()
    for i in range(len(seq) - 1):
        output.append(seq[i:i+n])
    return output

X = set(n_gram(2, s1, 'letter'))
Y = set(n_gram(2, s2, 'letter'))
print(X)
print(Y)

union = X | Y
intersection = X & Y
diff = X - Y
print(union)
print(intersection)
print(diff)

ansX = "'se' is in X" if 'se' in X else "'se' is not in X"
ansY = "'se' is in Y" if 'se' in Y else "'se' is not in Y"
print(ansX)
print(ansY)
