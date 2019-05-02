import re
import gzip
from knock20 import jsons2dict

def extcatnames(text: str) -> list:
    mylist = []
    pattern = r'^\[\[Category:.*\]\]'
    pattern = r'^\[\[Category:(?P<catname>.+?)(?:\|.*)?\]\]'

    for m in re.finditer(pattern, text, flags=(re.MULTILINE)):
        # newstr = m.group(0).lstrip('[[Category:').rstrip(']]')
        # mylist.append(newstr)
        print(m.group('catname'))
        mylist.append(m.group('catname'))
    return mylist


def main():
    with gzip.open('jawiki-country.json.gz','rt',encoding = 'utf-8') as infiles:
        data = jsons2dict(infiles,'イギリス')
        catnames = extcatnames(data['text'])
    return

if __name__=='__main__':
    main()
