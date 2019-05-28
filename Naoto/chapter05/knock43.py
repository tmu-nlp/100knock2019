'''
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．\
    ただし，句読点などの記号は出力しないようにせよ．
'''

from knock41 import load_cabocha_iter


def main():
    out_path = 'Dependency_noun_verb.txt'
    with open(out_path, "w") as f:
        for chunks in load_cabocha_iter():
            for chunk in chunks:
                if chunk.dst == -1:
                    continue
                if all(morph.pos != '名詞' for morph in chunk.morphs):
                    continue
                if all(morph.pos != '動詞' for morph in chunks[chunk.dst].morphs):
                    continue
                src = chunk.normalized_surface()
                dst = chunks[chunk.dst].normalized_surface()
                f.write(f'{src}\t{dst}\n')


if __name__ == "__main__":
    main()
