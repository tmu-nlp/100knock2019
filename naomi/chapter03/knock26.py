import re
import gzip
from knock20 import jsons2dict


def exttemplate(text: str) -> str:

    entries = re.split('\n+', text)

    p = re.compile(r"""
    (?P<quote>[('")]).*?(?P=quote)
    """, re.VERBOSE)

    for entry in entries:
        print(entry)
        m = p.match(entry)
        if m:
            print(m.group('quote'))
    return 'test'


def main():
    with gzip.open('jawiki-country.json.gz', 'rt', encoding='utf-8') as fs:

        data = jsons2dict(fs, 'イギリス')
        t = exttemplate(data['text'])
        print(t)
    return


if __name__ == '__main__':
    main()
