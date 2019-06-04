import re
from typing import Generator


def extract_sentence(filename: str = './nlp.txt') -> Generator[str, None, None]:
    """
    1文ごとに分割する
    """
    # (?<=[\.\;\:\!\?])\s(?=[A-Z])
    spliter = re.compile(
        r"""
        (?<=[\.\;\:\!\?]) # . ; : ! ? のどれかで終わる場所にマッチ
        \s
        (?=[A-Z]) # 大文字にマッチ
        """
    )
    for line in open(filename, 'r'):
        line = line.strip('\n')
        if not line:
            continue
        sentences = re.split(spliter, line)
        for sentence in sentences:
            yield sentence


def main():
    for sentence in extract_sentence():
        print(sentence)


if __name__ == '__main__':
    main()
