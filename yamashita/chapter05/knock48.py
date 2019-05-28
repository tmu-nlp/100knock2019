from knock41 import get_chunks_list

syntax_tree_list = []
for chunks in get_chunks_list('neko.txt.cabocha')[:10]:
    for chunk in chunks:
        syntax_list = []
        if chunk.has_pos('名詞') and chunk.dst != -1:
            syntax_list.append(chunk.no_sign_surface())
            dst = chunk.dst
            while dst != -1:
                syntax_list.append(chunks[dst].no_sign_surface())
                dst = chunks[dst].dst
            syntax_tree_list.append(syntax_list)
with open('result_48.txt', 'w', encoding='utf-8') as o_file:
    for syntax_tree in syntax_tree_list:
        tree = ' -> '.join(syntax_tree)
        print(f'{tree}', file=o_file)
