from knock41 import load_chunk_list
import re
from collections import defaultdict

output_path = "knock46.txt"

if __name__ == "__main__":
    pattern = re.compile('([\d,.，、．。,「」 ]+)')
    sentence_list = load_chunk_list("neko.txt.cabocha", 200)
    d = defaultdict(lambda: [[], []])
    for sentence in sentence_list:
        for verb_chunk in sentence:
            for verb_morph in verb_chunk.morphs:
                if verb_morph.pos != "動詞":
                    continue
                # 動詞の原形を辞書のキーにする
                key = verb_morph.base
                for i in verb_chunk.srcs:
                    for pp_chunk in sentence:
                        if pp_chunk.index != i:
                            continue
                        for pp_morph in pp_chunk.morphs:
                            if pp_morph.pos != "助詞":
                                continue
                            source_morph = pp_chunk.morphs[-1]
                            if source_morph.pos != "助詞":
                                source_morph = pp_chunk.morphs[-2]
                            # 助詞、助詞を含む文節を辞書で持っておく
                            d[key][0].append(source_morph.surface)
                            d[key][1].append(
                                pattern.sub("", pp_chunk.morphstr))

    with open(output_path, mode='w') as f:
        for key, pp_list in d.items():
            s = "{}".format(key)
            for pp_short_long in pp_list:
                s += "\t"
                for pp in list(set(pp_short_long)):
                    s += " {}".format(pp)
            s += "\n"
            print(s)
            f.write(s)

    '''
    $cat knock46.txt | grep -e "^始める" -e "^見る"
    始める	 で	 ここで
    見る	 は を	 吾輩は ものを
    '''
