from knock41 import importchunklists


def extractkakari(clist: list):

    with open('kakari.txt', 'w+', encoding='utf-8') as f:
        for chunks in clist:
            words = [chunk.text for chunk in chunks]
            for i, chunk in enumerate(chunks):
                if chunk.hasnoun() is True:
                    if chunks[chunk.dst].hasverb() is True:
                        print('\t'.join([words[i], words[chunk.dst]]), file=f)


def main():
    path = 'neko.txt.cabocha'
    clist = importchunklists(path)
    extractkakari(clist)


if __name__ == '__main__':
    main()
