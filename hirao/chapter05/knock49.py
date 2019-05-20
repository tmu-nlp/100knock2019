from knock41 import load_chunk_list
import re
pattern = re.compile('([\d,.，、．。, ]+)')


def knock49(sentence):
    l = []
    # 48と同じ手順で名詞から繋がるものを列挙
    for source_chunk in sentence:
        chunks = []
        if not "名詞" in [x.pos for x in source_chunk.morphs]:
            continue
        chunks.append(source_chunk)
        source_idx = source_chunk.index
        dst = source_chunk.dst
        while dst != -1:
            chunks.append(sentence[dst])
            source_idx = dst
            dst = sentence[dst].dst
        l.append(chunks)
    # print(l)
    '''
    [[
    [0] morphs: 吾輩は, dst: 5, srcs: [], 
    [5] morphs: 見た。, dst: -1, srcs: [0, 4]], [
    [1] morphs: ここで, dst: 2, srcs: [], 
    [2] morphs: 始めて, dst: 3, srcs: [1], 
    [3] morphs: 人間という, dst: 4, srcs: [2], 
    [4] morphs: ものを, dst: 5, srcs: [3], 
    [5] morphs: 見た。, dst: -1, srcs: [0, 4]], [
    [3] morphs: 人間という, dst: 4, srcs: [2], 
    [4] morphs: ものを, dst: 5, srcs: [3], 
    [5] morphs: 見た。, dst: -1, srcs: [0, 4]], [
    [4] morphs: ものを, dst: 5, srcs: [3], 
    [5] morphs: 見た。, dst: -1, srcs: [0, 4]]]
    [
    '''
    #
    ans = []
    for end_i in range(1, len(sentence)):
        for chunks in l:
            path = []
            # lの中でend_iで終わるもの
            if not end_i in [x.index for x in chunks]:
                continue
            for chunk in chunks:
                path.append(chunk.index)
                # end_i がくるまでのパスをpathに保存
                if chunk.index == end_i:
                    if len(path) > 1:
                        ans.append(path)
                    break
    # print(ans)
    '''
    [[1, 2], [1, 2, 3], [1, 2, 3, 4], [3, 4], [0, 5], [1, 2, 3, 4, 5], [3, 4, 5], [4, 5]]
    '''
    # パスから、共通部分がないものを探す
    for paths in ans:
        end_i = paths[-1]
        # 末尾が名詞を含むか文の終わり以外の場合、表示しない
        if not (end_i == len(sentence) - 1 or "名詞" in [morph.pos for morph in sentence[end_i].morphs]):
            continue

        part = []
        for ref_paths in ans:
            if ref_paths[-1] == end_i:
                if len(set(paths[:-1]) | set(ref_paths[:-1])) == len(set(paths[:-1])) + len(set(ref_paths[:-1])):
                    # 重複してる部分がない2つをpartに入れる
                    part.append(ref_paths)
        symbol = "X"
        # 名詞をX、Yに置き換えたりする
        # 重なっている部分があるもの
        if len(part) > 0:
            for ref_paths in part:
                if ref_paths[0] > paths[0]:
                    symbol = "X"
                    s = ""
                    # 1つ目
                    for i, index in enumerate(paths[:-1]):
                        for morph in sentence[index].morphs:
                            if symbol == "X" and morph.pos == "名詞":
                                s += symbol
                                symbol = "Y"
                            else:
                                s += pattern.sub("", morph.surface)
                        if i != len(paths[:-1]) - 1:
                            s += " -> "
                    # 2つ目
                    s += " | "
                    for i, index in enumerate(ref_paths[:-1]):
                        for morph in sentence[index].morphs:
                            if symbol == "Y" and morph.pos == "名詞":
                                s += symbol
                                symbol = "Z"
                            else:
                                s += pattern.sub("", morph.surface)
                        if i != len(ref_paths[:-1]) - 1:
                            s += " -> "
                    # 最後
                    last = pattern.sub("", sentence[paths[-1]].morphstr)
                    s += f" | {last}"
                    print(s)
        # 1つのパスを表示するもの
        else:
            s = ""
            for i, index in enumerate(paths):
                if i == 0:
                    for morph in sentence[index].morphs:
                        if symbol == "X" and morph.pos == "名詞":
                            s += symbol
                            symbol = "Y"
                        else:
                            s += pattern.sub("", morph.surface)
                elif i == len(paths) - 1 and "名詞" in [morph.pos for morph in sentence[index].morphs]:
                        s += symbol
                        symbol = "Z"
                else:
                    s += pattern.sub("", sentence[index].morphstr)
                if i != len(paths) - 1:
                    s += " -> "
            print(s)


if __name__ == "__main__":
    sentence_list = load_chunk_list("neko.txt.cabocha")
    knock49(sentence_list[5])
