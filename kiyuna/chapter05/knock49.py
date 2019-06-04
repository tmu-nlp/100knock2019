'''
49. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．

- 問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を
  "->"で連結して表現する
- 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する

また，係り受けパスの形状は，以下の2通りが考えられる．

- 文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
- 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合:
  文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，
  文節kの内容を"|"で連結して表示

例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）
から，次のような出力が得られるはずである．

    Xは | Yで -> 始めて -> 人間という -> ものを | 見た
    Xは | Yという -> ものを | 見た
    Xは | Yを | 見た
    Xで -> 始めて -> Y
    Xで -> 始めて -> 人間という -> Y
    Xという -> Y
'''
import sys
from itertools import islice, combinations
from knock41 import cabocha_into_chunks, Chunk

d = dict()


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


class Chunk_normalized(Chunk):
    def __init__(self, chunk):
        self.morphs, self.dst, self.srcs = (*chunk,)
        self.norm = self.norm()

    def norm(self):
        # 各文節は（表層形の）形態素列で表現する
        clause = ''.join(m.surface for m in self.morphs if m.pos != '記号')
        return clause

    def has_pos(self, pos):
        res = []
        for i, m in enumerate(self.morphs):
            if m.pos == pos:
                res.append(i)
        return res

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

    def replace_noun(self, repl):
        # 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
        '''
        「書生というのは」-> 「XというXは」
        「第一毛をもって」-> 「第XXをもって」
        '''
        idxs = self.has_pos('名詞')
        l, r = idxs[0], idxs[-1] + 1    # half-open interval
        tmp = []
        for m in self.morphs[:l]:
            if m.pos != '記号':
                tmp.append(m.surface)
        tmp.append(repl)
        for m in self.morphs[r:]:
            if m.pos != '記号':
                tmp.append(m.surface)
        clause = ''.join(tmp)

        key = tuple(m.pos for m in self.morphs)
        d[key] = self.norm

        return clause


def replace_and_concat(idxs, chunks):
    head, *body, tail = map(lambda x: chunks[x], idxs)
    res = [head.replace_noun('X')]
    res += [c.norm for c in body]

    '''
    「おったY」「おY」「不Y」「つけてくれないY」「産まれたY」のような表現があるので，
    res += ['Y']
    と楽できない
    '''
    tmp = []
    flag = False
    for m in tail.morphs:
        if m.pos == '名詞':
            tmp.append('Y')
            flag = True
        else:
            if flag:
                break
            tmp.append(m.surface)
    res += [''.join(tmp)]

    # パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を
    # "->"で連結して表現する
    return ' -> '.join(res)


def replace_and_combine(part1, part2, tail, chunks):
    res = [None] * 3
    # パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を
    # "->"で連結して表現する
    for i, part in enumerate([part1, part2]):
        head, *body = map(lambda x: chunks[x], part)
        tmp = [head.replace_noun(repl='XY'[i])] + [c.norm for c in body]
        res[i] = ' -> '.join(tmp)
    res[2] = chunks[tail].norm
    return ' | '.join(res)


if __name__ == '__main__':

    res = []

    for chunks in cabocha_into_chunks():
        paths = []
        noun_idx = []
        chunks = tuple(map(Chunk_normalized, chunks.values()))

        # 名詞列のパス（idx の列）を作る
        for idx, dc in enumerate(chunks):
            if not dc.has_pos('名詞'):
                continue
            noun_idx.append(idx)
            if dc.dst == -1:
                paths.append([idx])
                continue
            tmp = [idx]
            dst = dc.dst
            while dst != -1:
                tmp.append(dst)
                dst = chunks[dst].dst
            paths.append(tmp)

        # i < j なる 2 つのパスを列挙
        for p1, p2 in combinations(paths, 2):
            p2_head = p2[0]     # 文節 j
            if p2_head in p1:
                '''
                文節iから構文木の根に至る経路上に文節jが存在する場合:
                文節iから文節jのパスを表示
                [1, 2, 3, 4, 5] [3, 4, 5] -> [1, 2, 3]
                '''
                p1_tail = p1.index(p2_head)
                idxs = p1[:p1_tail + 1]
                ans = replace_and_concat(idxs, chunks)
                res.append(ans + '\n')
            else:
                '''
                上記以外で，
                文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合:
                文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，
                文節kの内容を"|"で連結して表示
                [0, 5] [1, 2, 3, 4, 5] -> [0] [1, 2, 3, 4] [5]
                [0, 4, 5] [3, 4, 5] -> [0] [3] [4]
                '''
                for i, w1 in enumerate(p1[1:], start=1):
                    if w1 in p2:
                        part1, tail = p1[:i], p1[i]
                        part2 = p2[:p2.index(w1)]
                        break
                ans = replace_and_combine(part1, part2, tail, chunks)
                res.append(ans + '\n')

    sys.stdout.writelines(res)
    message(f'{len(res)} 行書き出しました')

    '''
    1 つの chunk に名詞が複数あるのを確認
    for k, v in d.items():
        if k.count('名詞') > 1:
            print(k, v, file=sys.stderr)
    '''
