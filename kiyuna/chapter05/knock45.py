'''
45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
ただし，出力は以下の仕様を満たすようにせよ．

- 動詞を含む文節において，最左の動詞の基本形を述語とする
- 述語に係る助詞を格とする
- 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

    始める  で
    見る    は を

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

- コーパス中で頻出する述語と格パターンの組み合わせ
- 「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
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


if __name__ == '__main__':
    res = []
    for chunks in cabocha_into_chunks():
        chunks = tuple(map(Chunk_normalized, chunks.values()))
        for dc in chunks:
            if not dc.has_pos('動詞'):
                continue
            srcs = []
            for sc_idx in dc.srcs:
                # 述語に係る助詞を格とする
                for m in chunks[sc_idx].get_pos('助詞'):
                    srcs.append(m.base)
            # 動詞を含む文節において，最左の動詞の基本形を述語とする
            base = dc.get_pos('動詞')[0].base
            # 述語に係る助詞（文節）が複数あるときは，
            # すべての助詞をスペース区切りで辞書順に並べる
            srcs.sort()
            particles = " ".join(srcs)
            if srcs:
                res.append(f'{base}\t{particles}\n')
    sys.stdout.writelines(res)
    message(f'{len(res)} 行書き出しました')
