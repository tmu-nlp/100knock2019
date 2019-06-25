import random
from tqdm import tqdm
from collections import defaultdict
import joblib


vocab = defaultdict(lambda: len(vocab))
with open('./chapter09/context.txt', 'w') as f:
    for line in tqdm(open('./chapter09/corpus81.txt', 'r').readlines()):
        words = line.rstrip().split(' ')
        for i, word in enumerate(words):
            vocab[word]
            d = random.randint(1, 5)
            for j in range(1, d + 1):
                if i+j < len(words):
                    f.write(f'{word}\t{words[i+j]}\n')
                if i-j >= 0:
                    f.write(f'{word}\t{words[i-j]}\n')
    
joblib.dump(dict(vocab), 'vocab')