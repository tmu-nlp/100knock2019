'''
46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）を
タブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

- 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
- 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

    始める  で      ここで
    見る    は を   吾輩は ものを
'''
import sys
from knock41 import cabocha_into_chunks, Chunk


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


class Chunk_normalized(Chunk):
    def __init__(self, chunk):
        self.morphs, self.dst, self.srcs = (*chunk,)
        self.norm = self.norm()

    def norm(self):
        clause = ''.join(m.surface for m in self.morphs if m.pos != '記号')
        return clause

    def has_pos(self, pos):
        for m in self.morphs:
            if m.pos == pos:
                return True
        return False

    def get_pos(self, pos):
        res = []
        for m in self.morphs:
            if m.pos == pos:
                res.append(m)
        return res


if __name__ == "__main__":
    res = []
    for chunks in cabocha_into_chunks():
        chunks = tuple(map(Chunk_normalized, chunks.values()))
        for dc in chunks:
            if not dc.has_pos('動詞'):
                continue
            # 動詞を含む文節において，最左の動詞の基本形を述語とする
            v_base = dc.get_pos('動詞')[0].base

            srcs = []
            for sc_idx in dc.srcs:
                # 述語に係る助詞を格とする
                ms = chunks[sc_idx].get_pos('助詞')
                if ms:
                    # 文節内に助詞が複数ある場合は最も右のものを選ぶ
                    srcs.append((ms[-1].base, chunks[sc_idx].norm))
            if srcs:
                # 述語に係る助詞（文節）が複数あるときは，
                # すべての助詞をスペース区切りで辞書順に並べる
                srcs.sort()
                pb, pc = zip(*srcs)
                p_base = " ".join(pb)
                # 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
                # 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
                clause = " ".join(pc)
                res.append(f'{v_base}\t{p_base}\t{clause}\n')
    sys.stdout.writelines(res)
    message(f'{len(res)} 行書き出しました')
