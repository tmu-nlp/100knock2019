from knock41 import importchunklists


def extract_kinou(clist: list):

    with open('kinoudousi.txt', 'w+', encoding='utf-8') as f:

        # 1文ずつ
        for chunks in clist:
            # １文節ずつ
            for chunk in chunks:

                # 動詞にかかる「サ変接続名詞＋を」のChunkオブジェクトをリスト
                sahen_chunks = [chunks[i] for i in chunk.srcs
                                # この文節自身が動詞を持つとき
                                if (chunk.hasverb() is True)
                                # この文節にかかる文節が「名詞（サ変）＋を」のとき
                                and (chunks[i].hassahen() is True)]

                for sahen_chunk in sahen_chunks:
                    # 述語にかかる項の取り出し
                    kou_chunks = [chunks[i] for i
                                  in chunks[sahen_chunk.dst].srcs
                                  if (chunks[i] is not sahen_chunk)]

                    # 項のchunkオブジェクトを、助詞の辞書順に並び替え
                    sorted_kou = sorted(kou_chunks, key=lambda x: x.pp)

                    # 項に含まれる助詞のリスト
                    pp = [chunk.pp for chunk in sorted_kou]

                    # 項のリスト
                    kou = [chunk.text for chunk in sorted_kou]

                    if pp == [''] or pp == []:
                        continue
                    if kou == []:
                        continue
                    print('\t'.join(
                          [sahen_chunk.text +
                           chunks[sahen_chunk.dst].predicate(),
                           ' '.join(pp),
                           ' '.join(kou)]),
                          file=f)


def main():
    path = 'neko.txt.cabocha'
    clist = importchunklists(path)
    extract_kinou(clist)


if __name__ == '__main__':
    main()
