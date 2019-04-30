import re
import gzip
from knock20 import jsons2dict

def extcatnames(text: str) -> list:
    mylist = []
    pattern = r'^\[\[Category:.*\]\]'

    for m in re.finditer(pattern, text, flags=(re.MULTILINE)):
        newstr = m.group(0).lstrip('[[Category:').rstrip(']]')
        mylist.append(newstr)
    return mylist


def main():
    with gzip.open('jawiki-country.json.gz','rt',encoding = 'utf-8') as infiles:
        data = jsons2dict(infiles,'イギリス')
        catnames = extcatnames(data['text'])
        print(catnames)
    return

if __name__=='__main__':
    main()
