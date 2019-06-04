import re

with open('nlp_sentences.txt', 'w') as f:
    for line in open('./nlp.txt', 'r'):
        line = line.strip('\n')
        print(re.sub(r'([.:;!?])\s([A-Z])', r'\1\n\2', line), file=f)

