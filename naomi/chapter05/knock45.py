from knock41 import importchunklists


def extract_kaku(clist: list):

    with open('kaku.txt', 'w+', encoding='utf-8') as f:

        # 1文ずつ
        for chunks in clist:
            # １文節ずつ
            for chunk in chunks:
                # この文節が動詞を持つならば、この文節にかかる文節に含まれる助詞をリスト
                pp = [chunks[i].pp for i in chunk.srcs
                      if chunk.hasverb() is True]

                # 助詞を辞書順に並び替え
                pp.sort()

                # 動詞にかかる助詞が存在するならばファイルに動詞、助詞を書き込み
                if pp != []:
                    print('\t'.join([chunk.predicate(), ' '.join(pp)]), file=f)


def main():
    path = 'neko.txt.cabocha'
    clist = importchunklists(path)
    extract_kaku(clist)

# grep "^与える" kaku.txt | sort | uniq -c | sort -n -r > 与える
# grep "^する" kaku.txt | sort | uniq -c | sort -n -r > する


if __name__ == '__main__':
    main()
