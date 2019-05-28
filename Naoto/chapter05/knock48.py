'''
48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
'''

from knock41 import cabocha_Chunk_read


def main():
    path = "noun_to_root.txt"
    count = 0
    with open(path, "w") as f:
        for chunks in cabocha_Chunk_read():
            for chunk in chunks:
                if chunk.dst == -1:
                    continue
                if all(m.pos != "名詞" for m in chunk.morphs):
                    continue
                f.write(chunk.normalized_surface())
                i = chunk.dst
                while i != -1:
                    f.write(" -> " + chunks[i].normalized_surface())
                    i = chunks[i].dst
                f.write("\n")


if __name__ == '__main__':
    main()
