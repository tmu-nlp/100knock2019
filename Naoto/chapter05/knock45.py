'''
45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．

動詞を含む文節において，最左の動詞の基本形を述語とする
述語に係る助詞を格とする
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で
見る    は を
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語と格パターンの組み合わせ
「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
'''


from knock41 import load_cabocha_iter


def main():
    path = "case_pattern.txt"
    with open(path, "w") as f:
        for chunks in load_cabocha_iter():
            case_patterns = {}
            # {id: [動詞の基本形, [助詞, 助詞,...]]}
            for chunk in chunks:
                if chunk.dst == -1:
                    continue
                particles = [chunk.morphs[-1].surface]
                # particles = [morph.surface for morph in chunk.morphs if morph.pos == '助詞']
                verbs = [morph.base for morph in chunks[chunk.dst].morphs if morph.pos == '動詞']
                if not particles or not verbs:
                    continue
                if chunk.dst not in case_patterns:
                    case_patterns[chunk.dst] = [verbs[0], particles]
                else:
                    case_patterns[chunk.dst][1].extend(particles)
            for value in case_patterns.values():
                f.write(f'{value[0]}\t{" ".join(sorted(value[1]))}\n')


if __name__ == "__main__":
    main()


'''
sort case_pattern.txt | uniq -c | sort -n -r | head
grep "^する\s" case_pattern.txt | sort | uniq -c | sort -n -r | head
'''