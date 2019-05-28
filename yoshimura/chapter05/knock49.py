'''
49. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．

問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
また，係り受けパスの形状は，以下の2通りが考えられる．

文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文
節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示
例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
'''
from knock41 import Chunk, get_chunk_list
from itertools import combinations
from typing import List


def get_path_to_root(chunks: List[Chunk], chunk: Chunk) -> List[Chunk]:
    '''chunkから根までに通るChunkオブジェクトのリストを返す'''
    dst = chunk.dst
    path = []
    if dst == -1:
        return path
    while dst != -1:
        path.append(chunks[dst])
        dst = chunks[dst].dst
    return path


def path_to_text(path: List[Chunk]) -> str:
    '''
    Chunkオブジェクトを要素とするリストを受け取り
    そのオブジェクトの表層形を
    '-> surface -> surface -> surface'
    の形にして返す
    '''
    result = ''
    for chunk in path:
        result += ' -> ' + chunk.normalized_surface()
    return result


def get_path_to_cross(path: List[Chunk], cross: Chunk) -> List[Chunk]:
    '''pathからcrossまでのオブジェクトを要素とするリストを返す'''
    result = []
    for chunk in path:
        result.append(chunk)
        if chunk is cross:
            return result
        return result


with open('result49_', 'w') as f:
    for chunks in get_chunk_list("neko.txt.cabocha"):
        # 名詞を含む文節の組み合わせを取得
        pairs = combinations([c for c in chunks if c.check_pos('名詞')], 2)

        for pair in pairs:
            x, y = pair

            # 根までのパスを取得
            x_path = get_path_to_root(chunks, x)
            y_path = get_path_to_root(chunks, y)

            # 根までの経路で共通する文節を取得
            diff = list(set(x_path) & set(y_path))

            # XとYの助詞があれば取得
            X_particle = x.get_surfaces('pos', '助詞')
            X_particle = X_particle[-1] if X_particle else ''
            Y_particle = y.get_surfaces('pos', '助詞')
            Y_particle = Y_particle[-1] if Y_particle else ''

            # xから根までのパスにyが存在する
            if y in x_path:
                path = path_to_text(x_path[:x_path.index(y)])  # yまでのパス

                f.write(f'X{X_particle}')
                if path:
                    f.write(f'{path}')
                f.write(f' -> Y\n')

            # yから根までのパスにxが存在する
            elif x in y_path:
                path = path_to_text(y_path[:y_path.index(x)])  # xまでのパス

                f.write(f'X{X_particle}')
                if path:
                    f.write(f'{path}')
                f.write(f' -> Y\n')

            # xとyが根に至る経路上の文節kで交わる場合
            elif len(diff) >= 1:
                # 最初に交差する文節を取得
                cross = diff[0]

                # 交差する文節までのパスをそれぞれ取得
                x_path = path_to_text(x_path[:x_path.index(cross)])
                y_path = path_to_text(y_path[:y_path.index(cross)])
                cross = cross.normalized_surface()

                # パスを書き込む
                f.write(f'X{X_particle}')
                if x_path:
                    f.write(f'{x_path}')
                f.write(" | ")
                f.write(f'Y{Y_particle}')
                if y_path:
                    f.write(f'{y_path}')
                f.write(" | ")
                f.write(f'{cross} \n')
