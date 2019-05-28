# 45. 動詞の格パターンの抽出
# 今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
# 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
# ただし，出力は以下の仕様を満たすようにせよ．
#  - 動詞を含む文節において，最左の動詞の基本形を述語とする
#  - 述語に係る助詞を格とする
#  - 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

from knock41 import load_chunk_cabocha, Chunk
from typing import List, Dict

C = List[Chunk]
T = List[C]


def get_case_pattern_of_verb() -> None:
    for sentence in load_chunk_cabocha():
        case_pattern = {}  # type: Dict[int, Dict[str, List[str]]]
        # 例
        #   {1: {'生れる': ['で']}, 4: {'つく': ['か', 'が']}}
        #   {5: {'泣く': ['で']}, 7: {'する': ['て', 'だけ', 'は']}}
        for chunk in sentence:
            if chunk.dst == -1:
                continue
            # 助詞の探索
            pp = [m.surface for m in chunk.morphs if m.pos == "助詞"]
            # 述語の探索 (助詞の掛かり先から探索する)
            verbs = [m.base for m in sentence[chunk.dst].morphs if m.pos == "動詞"]

            if verbs == [] or pp == []:
                continue

            if chunk.dst not in case_pattern:
                # 最左の動詞をキーとした助詞のリストを、文節の係り先をキーとして追加する
                case_pattern[chunk.dst] = {verbs[0]: pp}
            else:
                # 既存の場合、助詞のリストを追加する
                case_pattern[chunk.dst][verbs[0]].extend(pp)

        for dic in case_pattern.values():
            for verb, pp in dic.items():
                print(f"{verb}\t{' '.join(sorted(pp))}")


if __name__ == "__main__":
    get_case_pattern_of_verb()

# 実行
# python knock45.py > result.txt
#
# $ sort result.txt | uniq -c | sort -r | head
# 565 云う      と
# 442 する      を
# 249 思う      と
# 199 ある      が
# 189 なる      に
# 174 する      に
# 173 見る      て
# 127 する      と
# 117 する      が
# 105 する      に を
#
# $ grep "^する\s" result.txt | sort | uniq -c | sort -r | head
# 442 する      を
# 174 する      に
# 127 する      と
# 117 する      が
# 105 する      に を
#  86 する      て を
#  59 する      は
#  58 する      て
#  57 する      が を
#  48 する      から
#
# $ grep "^見る\s" result.txt | sort | uniq -c | sort -r | head
# 173 見る      て
#  94 見る      を
#  21 見る      て て
#  20 見る      から
#  18 見る      て を
#  14 見る      と
#  12 見る      から て
#  12 見る      で
#  11 見る      て は
#   8 見る      に
#
# $ grep "^与える\s" result.txt | sort | uniq -c | sort -r | head
#   3 与える    に を
#   2 与える    て に は を
#   1 与える    けれども に は を
#   1 与える    だけ で に を
#   1 与える    たり て に を
#   1 与える    に に対して のみ は は も
#   1 与える    か じゃあ て と は を
#   1 与える    か として を
#   1 与える    が て て と に は は を
#   1 与える    て に に は を
