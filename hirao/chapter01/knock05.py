def n_gram(n, seq, output_type='word'):
    output = []
    if output_type == 'word':
        seq = seq.split()
    for i in range(len(seq) - 1):
        output.append(seq[i:i+n])
    return output


s = "I am an NLPer"
print(n_gram(2, s))
print(n_gram(2, s, 'letter'))
