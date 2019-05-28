from knock41 import get_chunks_list

with open('result_45.txt', 'w', encoding='utf-8') as o_file:
    for chunks in get_chunks_list('neko.txt.cabocha'):
        patterns = {}
        for chunk in chunks:
            # 動詞から助詞を探す
            if chunk.has_pos('動詞'):
                predicate = chunk.get_allsurfaces_base('pos', '動詞')[0]
                particles = []
                for src in chunk.srcs:
                    if len(chunks[src].get_allsurfaces_base('pos', '助詞')) > 0:
                        particles.append(
                            chunks[src].get_allsurfaces_base('pos', '助詞').pop())
                if len(particles) > 0:
                    txt = ' '.join(sorted(particles))
                    print(f'{predicate}\t{txt}', file=o_file)

            # 助詞から動詞を探す
            # if chunk.dst == -1:
            #     continue
            # particles = [
            #     morph.surface for morph in chunk.morphs if morph.pos == '助詞']
            # predicates = [
            #     morph.base for morph in chunks[chunk.dst].morphs if morph.pos == '動詞']
            # # for morph in chunk.morphs:
            # #     if morph.pos == '助詞':
            # #         particles.append(morph.surface)

            # # for morph in chunks[chunk.dst].morphs:
            # #     if morph.pos == '動詞':
            # #         predicates.append(morph.base)

            # if not particles or not predicates:
            #     continue

            # if chunk.dst not in patterns:
            #     patterns[chunk.dst] = [predicates[0], particles]
            # else:
            #     patterns[chunk.dst][1].extend(particles)

            # for pattern in patterns.values():
            #     print(
            #         f'{pattern[0]}\t{" ".join(sorted(pattern[1]))}', file=o_file)
