import re
import gzip
from collections import defaultdict
from knock20 import jsons2dict


def exttemplate(text: str) -> dict:

    td = defaultdict(lambda: 0)

    entries = re.split('\n+', text)

    p1 = re.compile(r"""
    (^\| (?P<key>.*?)
    \s=\s
    (?P<value>.*$))
    """, re.VERBOSE)
    p2 = re.compile(r"""
    '(?P<text>.*?)'
    """, re.VERBOSE)

    for entry in entries:
        m = p1.match(entry)
        if m:
            key = m.group('key').strip('|')
            key = key.strip()
            value = m.group('value').strip()
            # remove emphasis markers
            value2 = p2.sub(r'\g<text>', value)
            print('key: {0}, value: {1}'.format(key, value2))
            td[key] = value2

    return td


def main():
    with gzip.open('jawiki-country.json.gz', 'rt', encoding='utf-8') as fs:

        data = jsons2dict(fs, 'イギリス')
        t = exttemplate(data['text'])

    return None


if __name__ == '__main__':
    main()
