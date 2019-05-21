from knock41 import importchunklists


def extractkaku(clist: list):

    with open('kakuframe.txt', 'w+', encoding='utf-8') as f:

        # 1文ずつ
        for chunks in clist:
            # １文節ずつ
            for chunk in chunks:
                # この文節にかかる項のchunkオブジェクトをリスト
                kou_chunk = [chunks[i] for i in chunk.srcs
                             if (chunk.hasverb() is True)   # この文節が動詞を持つとき
                             and (chunks[i].pp != '')]      # この文節にかかる項が助詞を持つとき

                # 項のchunkオブジェクトを、助詞の辞書順に並び替え
                sorted_kou = sorted(kou_chunk, key=lambda x: x.pp)

                # 項に含まれる助詞のリスト
                pp = [chunk.pp for chunk in sorted_kou]

                # 項のリスト
                kou = [chunk.text for chunk in sorted_kou]

                # 動詞にかかる助詞が存在するならばファイルに動詞、助詞を書き込み
                if pp != []:
                    print('\t'.join([chunk.predicate(),
                          ' '.join(pp), ' '.join(kou)]), file=f)


def main():
    path = 'neko.txt.cabocha'
    clist = importchunklists(path)
    extractkaku(clist)


if __name__ == '__main__':
    main()
