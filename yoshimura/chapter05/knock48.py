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
from knock41 import get_chunk_list

with open('result48', 'w') as f:
    for chunks in get_chunk_list("neko.txt.cabocha"):
        for chunk in chunks:
            if not chunk.check_pos('名詞'):
                continue
            f.write(chunk.surface())
            dst = chunk.dst
            while dst != -1:
                f.write(f'-> {chunks[dst].surface()}')
                dst = chunks[dst].dst
            f.write('\n')