from knock41 import importchunklists


def extract_kakari(clist: list):

    with open('kakari.txt', 'w+', encoding='utf-8') as f:
        for chunks in clist:
            words = [chunk.text for chunk in chunks]
            for i, chunk in enumerate(chunks):
                # かかり先がない場合は出力しない
                if chunk.dst == -1:
                    continue
                print('\t'.join([words[i], words[chunk.dst]]), file=f)


def main():
    path = 'neko.txt.cabocha'
    clist = importchunklists(path)
    extract_kakari(clist)


if __name__ == '__main__':
    main()
