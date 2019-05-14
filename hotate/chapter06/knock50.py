import re
from typing import Generator


def extract_sentence(filename: str = './nlp.txt') -> Generator[str, None, None]:
    """
    1文ごとに分割する
    """
    # parser = re.compile(r'[A-Z].+?[\.\;\:\!\?](?=(?:\s[A-Z])|$)')
    spliter = re.compile(r'(?<=[\.\;\:\!\?])\s(?=[A-Z])')
    for line in open(filename, 'r'):
        line = line.strip('\n')
        if not line:
            continue
        # sentences = parser.findall(line)
        sentences = re.split(spliter, line)
        for sentence in sentences:
            yield sentence


if __name__ == '__main__':
    for sentence in extract_sentence():
        print(sentence)
