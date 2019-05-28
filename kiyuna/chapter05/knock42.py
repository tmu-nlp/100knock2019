'''
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
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


if __name__ == "__main__":
    res = []
    for chunks in cabocha_into_chunks():
        chunks = tuple(map(Chunk_normalized, chunks.values()))
        for c in chunks:
            if c.dst == -1:
                continue
            if c.norm and chunks[c.dst].norm:
                res.append(f'{c.norm}\t{chunks[c.dst].norm}\n')
    sys.stdout.writelines(res)
    message(f'{len(res)} 行書き出しました')


    ''' 記号の一覧を表示する
    from knock40 import cabocha_into_morphs
    symbols = {m.base for m in sum(cabocha_into_morphs(), []) if m.pos == '記号'}
    print(symbols, file=sys.stderr)

    => {'、', '？', 'Ｂ', '。', '』', 'Ｘ', '！', 'Ｋ', '『', '×',
        '＝', 'Ｔ', '々', '\u3000', '○', '…', 'α', '・', 'Ｃ',
        '※', 'Ｈ', '「', 'Ａ', 'Ｗ', 'Ｚ', '△', '」'}
    '''
