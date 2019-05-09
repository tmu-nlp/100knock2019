import re
import gzip
from collections import defaultdict
from knock20 import jsons2dict


def exttemplate(text: str) -> dict:

    td = defaultdict(lambda: 0)

    entries = re.split('\n+', text)

    p = re.compile(r"""
    (^\| (?P<key>.*?)
    \s=\s
    (?P<value>.*$))
    """, re.VERBOSE)

    for entry in entries:
        m = p.match(entry)
        if m:
            key = m.group('key').strip('|')
            key = key.strip()
            value = m.group('value').strip()
            print('key: {0}, value: {1}'.format(key, value))
            td[key] = value
    return td


def main():
    with gzip.open('jawiki-country.json.gz', 'rt', encoding='utf-8') as fs:

        data = jsons2dict(fs, 'イギリス')
        t = exttemplate(data['text'])
        print(t)
    return


if __name__ == '__main__':
    main()
