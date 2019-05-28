from knock41 import get_chunks_list

with open('result_46.txt', 'w', encoding='utf-8') as o_file:
    for chunks in get_chunks_list('neko.txt.cabocha'):
        for chunk in chunks:
            # 動詞から助詞を探す
            if chunk.has_pos('動詞'):
                predicate = chunk.get_allsurfaces_base('pos', '動詞')[0]
                particles = []
                phrases = []
                pairs = []
                for src in chunk.srcs:
                    if len(chunks[src].get_allsurfaces_base('pos', '助詞')) > 0:
                        particles.append(
                            chunks[src].get_allsurfaces_base('pos', '助詞').pop())
                        phrases.append(chunks[src].surface())
                        pairs.append([chunks[src].get_allsurfaces_base(
                            'pos', '助詞').pop(), chunks[src].surface()])
                if len(particles) > 0:
                    pairs = sorted(pairs, key=lambda x: x[0])
                    sorted_particles = []
                    sorted_phrases = []
                    for i in range(len(pairs)):
                        sorted_particles.append(pairs[i][0])
                        sorted_phrases.append(pairs[i][1])
                    txt = ' '.join(sorted_particles)
                    phrase = ' '.join(sorted_phrases)
                    print(f'{predicate}\t{txt}\t{phrase}', file=o_file)
