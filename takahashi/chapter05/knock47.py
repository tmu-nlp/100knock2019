# 47. 機能動詞構文のマイニング
# 動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．
# - 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
# - 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
# - 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
# - 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）

from knock41 import load_chunk_cabocha, Chunk
from typing import List, Dict

# 機能動詞 (軽動詞 : light verb) を探す
# 動詞を検索し, 動詞の係り元から助詞を含むリストを作成する
# 助詞のリストから「サ変接続名詞+を」を探し、軽動詞にして出力する
def mining_light_verb_syntax():
    for chunks in load_chunk_cabocha():
        for i, chunk in enumerate(chunks):
            if chunk.srcs == []:
                continue

            # 動詞の探索
            verbs = [morph.base for morph in chunk.morphs if morph.pos == "動詞"]
            if verbs == []:
                continue

            # 助詞を含む文節のリスト
            phrases_containing_particle = []
            for src in chunk.srcs:
                # 参照先の文節に助詞が一つでも含まれていれば、参照先の文節を追加する
                if any(morph.pos == "助詞" for morph in chunks[src].morphs):
                    phrases_containing_particle.append(chunks[src])
            if phrases_containing_particle == []:
                continue

            # 「サ変接続名詞+を」となる文節を探し助詞を含む文節のリストから除去する
            light_verb = ""
            for phrase in phrases_containing_particle:
                for i in range(len(phrase.morphs) - 1):
                    if (
                        phrase.morphs[i].pos1 == "サ変接続"
                        and phrase.morphs[i + 1].surface == "を"
                    ):
                        light_verb = f"{phrase.morphs[i].surface}を{verbs[0]}"
                        phrases_containing_particle.remove(phrase)
                        break

            if light_verb == "":
                continue
            # 助詞と文節のリストの作成
            particles_and_phrases = []
            for phrase in phrases_containing_particle:
                for morph in phrase.morphs:
                    if morph.pos == "助詞":
                        particles_and_phrases.append([morph.surface, phrase.no_symbols()])
                        break

            particles = [pp[0] for pp in sorted(particles_and_phrases)]
            phrases = [pp[1] for pp in sorted(particles_and_phrases)]

            print(f"{light_verb}\t{' '.join(particles)}\t{' '.join(phrases)}")


if __name__ == "__main__":
    mining_light_verb_syntax()

# 実行
# Python knock47.py > result.txt

# cut -f1 result.txt | sort | uniq -c | sort -r | head
#   30 返事をする
#   21 挨拶をする
#   16 話をする
#   14 真似をする
#   13 喧嘩をする
#    8 質問をする
#    7 運動をする
#    6 注意をする
#    6 昼寝をする
#    6 話を聞く

# cut -f1,2 result.txt | grep -E "^.*\s.+" | sort | uniq -c | sort -r | head
#   4 挨拶をする	から
#   4 返事をする	と
#   3 返事をする	と は
#   3 挨拶をする	と
#   3 喧嘩をする	と
#   2 同情を表する	て と は
#   2 質問をかける	と は
#   2 休養を要する	は
#   2 返事をする	から と
#   2 質問をする	が
