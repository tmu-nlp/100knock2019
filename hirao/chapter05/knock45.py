from knock41 import load_chunk_list
import re
from collections import defaultdict

output_path = "knock45.txt"

if __name__ == "__main__":
    pattern = re.compile('([\d,.，、．。,「」 ]+)')
    sentence_list = load_chunk_list("neko.txt.cabocha", -1)
    d = defaultdict(lambda: [])
    for sentence in sentence_list:
        # 動詞を含む文節の抽出
        for verb_chunk in [chunk for chunk in sentence if "動詞" in [morph.pos for morph in chunk.morphs]]:
            for verb_morph in verb_chunk.morphs:
                if verb_morph.pos != "動詞":
                    continue
                # 動詞の原形を辞書のキーにする
                key = verb_morph.base
                for i in verb_chunk.srcs:
                    # 動詞にかかっている助詞を含む文節を抽出
                    for pp_chunk in [chunk for chunk in sentence if "助詞" in [morph.pos for morph in chunk.morphs]]:
                        for pp_morph in pp_chunk.morphs:
                            if pp_morph.pos != "助詞":
                                continue
                            # 助詞を辞書に追加
                            d[key].append(pattern.sub("", pp_morph.base))

    with open(output_path, mode='w') as f:
        for key, pp_list in d.items():
            pp_list = list(set(pp_list))
            # 辞書順で
            pp_list.sort()
            s = "{}\t".format(key)
            for pp in pp_list:
                s += " {}".format(pp)
            s += "\n"
            f.write(s)
# TODO?
# 連語の処理
# 〜に従ってが助詞になるなど
'''
$cat knock45.txt | grep -e "^する" -e "^見る" -e "^与える"

する	 か かい かも から が くらい ぐらい け けども けれど けれども こそ さ さえ し じゃ すら ずつ ぜ たって たり だけ だって だに だり ちゃ って つつ て で でも と という とか とかいう として とも と共に ども な ながら なぞ など なり なんか なんぞ なんて に にあたって において について にて によって に対し に対して に従って ね ねえ の ので のに のみ は ば ばかり へ ほど まで も ものの や やら よ より わ を をもって ん んで
見る	 か から が さえ し じゃ すら ぜ たり だけ って て で と という として な なあ ながら なんか なんぞ に について によって に従って ね ねえ の ので のに は ば ばかり へ べ まで も より を んで
与える	 か が け けれども じゃあ たり だけ て で と として に に対して のみ は ば も を
'''
