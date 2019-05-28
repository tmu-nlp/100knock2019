from knock41 import get_chunks_list


def get_chunk_path_to_root(sentence, start_chunk):
    chunk_path = []
    if start_chunk.dst == -1:
        return chunk_path
    dst = start_chunk.dst
    while dst != -1:
        chunk_path.append(sentence[dst])
        dst = sentence[dst].dst
    chunk_path.append(sentence[dst])
    return chunk_path


def get_cross_point_chunk(path1, path2):
    for chunk in path1:
        if chunk in path2:
            return chunk


with open('result_49.txt', 'w', encoding='utf-8') as o_file:
    for chunks in get_chunks_list('neko.txt.cabocha'):
        noun_chunk_list = []
        for chunk in chunks:
            if chunk.has_pos('名詞'):
                noun_chunk_list.append(chunk)

        for i in range(len(noun_chunk_list)-1):
            for j in range(len(noun_chunk_list))[i+1:]:
                path = get_chunk_path_to_root(chunks, noun_chunk_list[i])
                if len(path) == 0:
                    continue
                if noun_chunk_list[j] in path:
                    syntax_tree = []
                    syntax_tree.append(
                        noun_chunk_list[i].get_word_conversion_surface('名詞', 'X'))
                    k = 0
                    while path[k] != noun_chunk_list[j]:
                        syntax_tree.append(path[k].no_sign_surface())
                        k += 1
                    syntax_tree.append('Y')
                    print(' -> '.join(syntax_tree), file=o_file)
                else:
                    path2 = get_chunk_path_to_root(chunks, noun_chunk_list[j])
                    cross_chunk = get_cross_point_chunk(path, path2)
                    tree1 = []
                    tree2 = []
                    tree1.append(
                        noun_chunk_list[i].get_word_conversion_surface('名詞', 'X'))
                    tree2.append(
                        noun_chunk_list[j].get_word_conversion_surface('名詞', 'Y'))
                    if len(path) > 0:
                        k = 0
                        while path[k] != cross_chunk:
                            tree1.append(path[k].no_sign_surface())
                            k += 1
                    if len(path2) > 0:
                        k = 0
                        while path2[k] != cross_chunk:
                            tree2.append(path2[k].no_sign_surface())
                            k += 1
                    print(' | '.join(
                        [' -> '.join(tree1), ' -> '.join(tree2), cross_chunk.no_sign_surface()]), file=o_file)
