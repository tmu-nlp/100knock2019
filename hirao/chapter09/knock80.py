import bz2
from tqdm import tqdm_notebook as tqdm

def preprocess(sentence):
    tokens = []
    for word in sentence.rstrip().split():
        token = word.strip('''.,!?;:()[]'"''')
        if token == "":
            continue
        tokens.append(token)
    return " ".join(tokens)

if __name__ == "__main__":
    file_name = "enwiki-20150112-400-r100-10576.txt.bz2"
    with open("knock80.txt", "w") as fw:
        for sentence in tqdm(bz2.open(file_name, mode="rb")):
            fw.write(preprocess(sentence.decode('utf8')))