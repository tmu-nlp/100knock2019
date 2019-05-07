import re
import gzip
from knock20 import jsons2dict

def extcatnames(text: str) -> list:
    mylist = []

    pattern = r'(File|ファイル):(?P<filename>.+?)\|'

    for m in re.finditer(pattern, text, flags=(re.MULTILINE)):
        print(m.group('filename'))
        mylist.append(m.group('filename'))
    return mylist


def main():
    with gzip.open('jawiki-country.json.gz','rt',encoding = 'utf-8') as infiles:
        data = jsons2dict(infiles,'イギリス')
        catnames = extcatnames(data['text'])
    return

if __name__=='__main__':
    main()