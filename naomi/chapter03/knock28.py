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

    p3 = re.compile(r"""
    \[\[(?P<link>.*?)\]\]
    """, re.VERBOSE)

    p4 = re.compile(r"""
    \<          #<
    (ref)       #ref
    \>?         #> or nothing
    (?P<ref>.*?)<
    \/          # /
    (ref)?      # ref or nothing
    \>          # >
    """, re.VERBOSE)

    p4 = re.compile(r"""\<ref(?P<ref>.*?)\/(ref)?\>""")
    for entry in entries:
        m = p1.match(entry)
        if m:
            key = m.group('key').strip('|')
            key = key.strip()
            value = m.group('value').strip()
            # remove emphasis markers
            value2 = p2.sub(r'\g<text>', value)
            # remove iinternal link markers
            value3 = p3.sub(r'\g<link>', value2)
            # remove reference
            value4 = p4.sub(r'', value3)
            # remove line break
            value5 = re.sub(r'<br />', '', value4)
            # if value3 is not value4:
            #     print(value3)
            #     print(value4)
            print('key: {0}, value: {1}'.format(key, value5))
            td[key] = value5

    return td


def main():
    with gzip.open('jawiki-country.json.gz', 'rt', encoding='utf-8') as fs:

        data = jsons2dict(fs, 'イギリス')
        t = exttemplate(data['text'])

    return t


if __name__ == '__main__':
    main()
