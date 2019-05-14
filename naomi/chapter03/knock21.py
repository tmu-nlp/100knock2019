import re
import gzip
from knock20 import jsons2dict

def extcategories(text: str) -> list:
    mylist = []
    pattern = r'^\[\[Category:.*$'
    for m in re.finditer(pattern, text, flags=(re.MULTILINE)):
        mylist.append(m.group())
        print(m.group())
    return mylist


def main():
    with gzip.open('jawiki-country.json.gz','rt',encoding = 'utf-8') as infiles:
        data = jsons2dict(infiles,'イギリス')
        categories = extcategories(data['text'])
    return

if __name__=='__main__':
    main()
