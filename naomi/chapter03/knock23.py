import re
import gzip
from knock20 import jsons2dict

def extsections(text: str) -> list:
    pattern = r'^==.*=='

    sectionlist = []
    for m in re.finditer(pattern, text, flags=(re.MULTILINE)):
        level = int(m.group(0).count('=')/2 - 1)
        newstr = m.group(0).lstrip('='*level+'= ').rstrip(' ='+'='*level)
        # print(m.group(0),newstr,level)

        sectionlist.append([level, newstr])
    return sectionlist


def main():
    with gzip.open('jawiki-country.json.gz','rt',encoding = 'utf-8') as infiles:
        data = jsons2dict(infiles,'イギリス')
        sectionlist = extsections(data['text'])
        sectionlist.sort()
        print(sectionlist)
    return

if __name__=='__main__':
    main()
