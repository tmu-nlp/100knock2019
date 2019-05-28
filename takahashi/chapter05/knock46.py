# 46. 動詞の格フレーム情報の抽出
# 45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
# 45の仕様に加えて，以下の仕様を満たすようにせよ．
#  - 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
#  - 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる

from knock41 import load_chunk_cabocha, Chunk
from typing import List, Dict


class CasePattern:
    def __init__(self, id: int, verb: str, pp: List[str], chunk: str) -> None:
        self.id = id
        self.verb = verb  # 述語
        self.pp = pp  # 助詞のリスト
        self.chunk = [chunk]  # 文節のリスト


def get_case_frame_of_verb() -> None:
    for sentence in load_chunk_cabocha():
        case_pattern = []  # type: List[CasePattern]
        # 助詞を含む文節を探索していく
        for chunk in sentence:
            if chunk.dst == -1:
                continue
            # 助詞の探索
            pp = [m.surface for m in chunk.morphs if m.pos == "助詞"]
            # 述語の探索 (助詞の係り先から探索する)
            verbs = [m.base for m in sentence[chunk.dst].morphs if m.pos == "動詞"]

            if verbs == [] or pp == []:
                continue
            # 文節の係り先と一致する case.id のリスト
            if [case.id for case in case_pattern if case.id == chunk.dst] == []:
                # case.id に文節の係り先を保存する
                case_pattern.append(
                    CasePattern(chunk.dst, verbs[0], pp, chunk.no_symbols())
                )
            else:
                # 同じ述語へ係る格を追加する
                for case in case_pattern:
                    if case.id == chunk.dst:
                        case.pp.extend(pp)
                        case.chunk.append(chunk.no_symbols())
                        break

        for case in case_pattern:
            print(f"{case.verb}\t{' '.join(case.pp)}\t{' '.join(case.chunk)}")


if __name__ == "__main__":
    get_case_frame_of_verb()

"""
実行結果

生れる	で	どこで
つく	か が	生れたか 見当が
泣く	で	所で
する	て だけ は	泣いて いた事だけは
見る	は を	吾輩は ものを
始める	で	ここで
聞く	で	あとで
捕える	を	我々を
煮る	て	捕えて
食う	て	煮て
思う	から	なかったから
載せる	に	掌に
持ち上げる	て と	載せられて スーと
...
"""
