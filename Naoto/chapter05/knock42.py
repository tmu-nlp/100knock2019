'''
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．\
    ただし，句読点などの記号は出力しないようにせよ．
'''

from knock40 import Morph
from knock41 import Chunk
from knock41 import cabocha_Chunk_read


def main():
    out_path = 'Dependency.txt'
    with open(out_path, "w") as f:
        for chunks in cabocha_Chunk_read():
            for chunk in chunks:
                if chunk.dst == -1:
                    continue
                src = chunk.normalized_surface()
                dst = chunks[chunk.dst].normalized_surface()
                f.write(f'{src}\t{dst}\n')


if __name__ == "__main__":
    main()
