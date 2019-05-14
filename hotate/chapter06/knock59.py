import xml.etree.ElementTree as ET
from typing import Generator, Pattern

import regex


def search_np(parse_list: list,
              np_list: list,
              pattern: Pattern) -> None:
    """
    再帰的にS式を読み取り， NP が含まれるものを抽出する．
    """
    np = '(NP '
    np_len = len(np)
    for parse in parse_list:

        # (NP で始まるのか判定
        if parse[:np_len] == np:
            # (NP ) の中身を抽出
            parse_ext = parse[np_len:-1]
            np_list.append(parse_ext)
        else:
            # 次の ( にマッチさせるために外す
            parse_ext = parse[1:-1]

        # マッチした () 内に NP があるときのみ探索する気持ち
        search_np([s for s in regex.findall(pattern, parse_ext) if np in s], np_list, pattern)


def load_parse(filename: str = './nlp.txt.xml') -> Generator[ET.Element, None, None]:
    tree = ET.parse(filename)
    for parse in tree.iter('parse'):
        yield parse


def main():
    pattern = regex.compile(r'(?<rec>\((?:[^\(\)]+|(?&rec))*\))')
    for parse in load_parse():
        np_list = list()
        search_np([parse.text], np_list, pattern)
        for np in np_list:
            print(np)


if __name__ == '__main__':
    main()
