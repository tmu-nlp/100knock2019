'''
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
'''
from knock41 import get_chunk_list

src_dst_pairs = []
for chunks in get_chunk_list("neko.txt.cabocha"):
    for chunk in chunks:
        if chunk.dst != -1:
            src = chunk.normalized_surface()
            dst = chunks[chunk.dst].normalized_surface()
            if src != '' and dst != '':
                src_dst_pairs.append(f'{src}\t{dst}')

for pair in src_dst_pairs[:10]:
    print(pair)