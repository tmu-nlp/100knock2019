import json
from collections import OrderedDict
from collections import defaultdict
import pprint
import typing
import gzip

def json2dict(infile: typing.TextIO) -> dict:
    mydict = defaultdict(lambda:0)
    mydict = json.load(infile)
    return mydict

def jsons2dict(infiles: typing.TextIO,key: str) -> dict:
    for f in infiles:
        data = json.loads(f)
        if data['title']==key:
            return data
    return None
            

def showtext(mydict: dict, title: str):
    print(mydict[title])
    return


def main():
    with gzip.open('jawiki-country.json.gz','rt',encoding = 'utf-8') as infiles:
        data = jsons2dict(infiles,'イギリス')
        print(data['text'])

    return

if __name__=='__main__':
    main()
