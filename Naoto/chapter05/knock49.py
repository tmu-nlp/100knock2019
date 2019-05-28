from knock41 import load_cabocha_iter
from itertools import combinations


def obtain_direct_path(chunks, paths, i, j):
    '''
    名詞句ペア(文節番号がiとj)のパスを得る
    (文節iから構文木の根に至る経路上に文節jが存在する場合)
    '''
    path_str = chunks[i].xy_surface('X') + ' -> '
    for p in paths[i]:
        if p == j:
            path_str += chunks[p].xy_surface('Y')  # 問題文の実行結果に合わせる
            break
        else:
            path_str += chunks[p].normalized_surface() + ' -> '
    return path_str


def obtain_indirect_path(chunks, paths, i, j):
    '''
    名詞句ペア(文節番号がiとj)のパスを得る
    (文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合)
    '''
    # 文節iから文節kの直前までのパス
    path_str = chunks[i].xy_surface("X")
    for p in paths[i]:
        if p not in paths[j]:
            path_str += ' -> ' + chunks[p].normalized_surface()
            continue
        # 文節kに到達, 文節jから文節kの直前までのパス
        path_str += ' | ' + chunks[j].xy_surface('Y')
        for q in paths[j]:
            if p != q:
                path_str += ' -> ' + chunks[q].normalized_surface()
                continue
            # 文節kの内容
            path_str += ' | ' + chunks[p].normalized_surface()
            return path_str


def obtain_path_str(chunks, paths, i, j):
    '''
    名詞句ペア(文節番号がiとj)のパスの文字列を得る
    '''
    if j in paths[i]:
        return obtain_direct_path(chunks, paths, i, j)
    elif i in paths[j]:
        return obtain_direct_path(chunks, paths, j, i)
    else:
        return obtain_indirect_path(chunks, paths, i, j)


def main():
    path = "noun_path_2.txt"
    with open(path, "w") as f:
        for chunks in load_cabocha_iter():
            paths = {}  # ex) {0: [5], 1: [2, 3, 4, 5], 3: [4, 5], 4: [5]}
            for id_, chunk in enumerate(chunks):
                if all(m.pos != '名詞' for m in chunk.morphs):
                    continue
                current = chunk
                paths[id_] = []
                while current.dst != -1:
                    paths[id_].append(current.dst)
                    current = chunks[current.dst]
            for k, l in combinations(paths.keys(), 2):
                f.write(obtain_path_str(chunks, paths, k, l) + "\n")


if __name__ == "__main__":
    main()
