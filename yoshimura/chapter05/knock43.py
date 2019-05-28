'''
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
'''
from knock41 import get_chunk_list

np_vp = {}
for chunks in get_chunk_list("neko.txt.cabocha"):
    for chunk in chunks:
        if chunk.dst != -1 and chunk.check_pos('名詞') and chunks[chunk.dst].check_pos('動詞'):
            src = chunk.normalized_surface()
            dst = chunks[chunk.dst].normalized_surface()
            if src != '' and dst != '':
                np_vp.append(f'{src}\t{dst}')

for pair in np_vp[:10]:
    print(pair)