from knock41 import load_chunk_list
import re
from collections import defaultdict

output_path = "knock47.txt"

if __name__ == "__main__":
    pattern = re.compile('([\d,.，、．。,「」 ]+)')
    sentence_list = load_chunk_list("neko.txt.cabocha", -1)

    with open(output_path, mode='w') as f:
        for sentence in sentence_list:
            # 前からi番目のchunk(前後を使うため)
            for chunk_i in range(len(sentence)):
                chunk = sentence[chunk_i]
                for morph_i in range(len(chunk.morphs)):
                    morph = chunk.morphs[morph_i]
                    # インデントが深くなる & 長くなるので列挙
                    # サ変接続の名詞
                    if not morph.pos == "名詞" and morph.pos1 == "サ変接続":
                        continue
                    # その名詞の右側が「を」
                    if not (morph_i + 1 < len(chunk.morphs) and chunk.morphs[morph_i+1].surface == "を"):
                        continue
                    # その右の文節が動詞
                    if not (chunk_i + 1 < len(sentence) and sentence[chunk_i+1].morphs[0].pos == "動詞"):
                        continue
                    # 動詞が原形か否か
                    if not sentence[chunk_i+1].morphs[0].surface == sentence[chunk_i+1].morphs[0].base:
                        continue
                    base_str = pattern.sub(
                        "", chunk.morphstr + sentence[chunk_i+1].morphs[0].surface)
                    # この名詞+を+動詞にかかる文節を列挙
                    l = []
                    l.extend(chunk.srcs)
                    l.extend(sentence[chunk_i+1].srcs)
                    # 自分を除くユニーク
                    l = list(set(l))
                    if chunk_i in l:
                        l.remove(chunk_i)
                    if chunk_i+1 in l:
                        l.remove(chunk_i+1)

                    pp_list = []
                    chunk_list = []
                    for i in l:
                        # 列挙した文節を、最後の助詞と本体に分ける
                        source_morph = sentence[i].morphs[-1]
                        if source_morph.pos != "助詞" and len(sentence[i].morphs) > 1:
                            source_morph = sentence[i].morphs[-2]
                        if source_morph.pos == "助詞":
                            pp_list.append(pattern.sub(
                                "", source_morph.surface))
                            chunk_list.append(pattern.sub(
                                "", sentence[i].morphstr))
                    if len(pp_list) == 0:
                        break
                    s = base_str + "\t"
                    for pp in pp_list:
                        s += pp + " "
                    # 余分なスペース除去
                    s = s[:-1]
                    s += "\t"
                    for chunk_str in chunk_list:
                        s += chunk_str + " "
                    s = s[:-1]
                    s += "\n"
                    f.write(s)
