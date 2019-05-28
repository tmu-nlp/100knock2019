from knock41 import get_chunks_list

path = 'neko.txt.cabocha'
for sentence in get_chunks_list(path):
    for chunk in sentence:
        if chunk.dst != -1:
            if chunk.has_pos('名詞') and sentence[chunk.dst].has_pos('動詞'):
                src = chunk.no_sign_surface()
                dst = sentence[chunk.dst].no_sign_surface()
                if src != '' and dst != '':
                    print(f'{src}\t{dst}')
