'''
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
46のプログラムを以下の仕様を満たすように改変せよ．

- 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
- 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，
  最左の動詞を用いる
- 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
- 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）

例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，
以下の出力が得られるはずである．

    返事をする      と に は        及ばんさと 手紙に 主人は

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

- コーパス中で頻出する述語（サ変接続名詞+を+動詞）
- コーパス中で頻出する述語と助詞パターン
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

    def has_sahen_wo(self):
        for m1, m2 in zip(self.morphs, self.morphs[1:]):
            if [m1.pos1, m2.pos, m2.base] == ['サ変接続', '助詞', 'を']:
                return True
        return False


if __name__ == '__main__':
    res = []
    for chunks in cabocha_into_chunks():
        chunks = tuple(map(Chunk_normalized, chunks.values()))
        for dc in chunks:
            if not dc.has_pos('動詞'):
                continue
            # 動詞を含む文節において，最左の動詞の基本形を述語とする
            v_base = dc.get_pos('動詞')[0].base

            srcs = []
            # 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
            failed = True
            for sc_idx in dc.srcs:
                if chunks[sc_idx].has_sahen_wo():
                    v_base = chunks[sc_idx].norm + v_base
                    failed = False
                else:
                    # 述語に係る助詞を格とする
                    ms = chunks[sc_idx].get_pos('助詞')
                    if ms:
                        # 文節内に助詞が複数ある場合は最も右のものを選ぶ
                        srcs.append((ms[-1].base, chunks[sc_idx].norm))

            if failed:      # 「サ変接続名詞+を+動詞」がなかった
                continue

            if not srcs:    # 助詞がなかった
                continue

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
