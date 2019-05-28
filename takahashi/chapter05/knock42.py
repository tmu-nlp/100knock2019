# 42. 係り元と係り先の文節の表示
# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

from knock41 import load_chunk_cabocha


def main() -> None:
    for chunks in load_chunk_cabocha():
        for chunk in chunks:
            if chunk.dst == -1:
                continue

            # Chunk.no_symbols() で記号を取り除いた形式にする
            src = chunk.no_symbols()
            dst = chunks[chunk.dst].no_symbols()

            # src, dst が空でなければ出力
            if src != "" and dst != "":
                print(f"{src} {dst}")


if __name__ == "__main__":
    main()

"""
実行結果

吾輩は 猫である
名前は 無い
まだ 無い
どこで 生れたか
生れたか つかぬ
とんと つかぬ
見当が つかぬ
何でも 薄暗い
薄暗い 所で
じめじめした 所で
所で 泣いて
ニャーニャー 泣いて
泣いて 記憶している
いた事だけは 記憶している
吾輩は 見た
ここで 始めて
始めて 人間という
人間という ものを
ものを 見た
...

"""
