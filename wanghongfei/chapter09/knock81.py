from tqdm import tqdm

countries_set = set()
for line in open('./chapter09/country.txt', 'r').readlines():
    if len(line) > 2:
        countries_set.add(line.strip())

with open('./chapter09/corpus81.txt', 'w') as f:
    for line in tqdm(open('./chapter09/corpus.txt', 'r')):
        for country in countries_set:
            line = line.replace(country, country.replace(' ', '_'))
        f.write(line)