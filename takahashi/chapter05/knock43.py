# 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
# 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

from knock41 import load_chunk_cabocha


def main() -> None:
    for chunks in load_chunk_cabocha():
        for chunk in chunks:
            if chunk.dst == -1:
                continue

            # 名詞と動詞を含む文節のフラグ
            exist_noun = False
            exist_verb = False

            # 現在の文節内に名詞が存在するかの判定
            for m in chunk.morphs:
                if m.pos == "名詞":
                    exist_noun = True

            # 現在の文節の掛かり先が動詞であるかの判定
            for m in chunks[chunk.dst].morphs:
                if m.pos == "動詞":
                    exist_verb = True

            # 両方のフラグが True の場合に出力する
            if exist_noun and exist_verb:
                src = chunk.no_symbols()
                dst = chunks[chunk.dst].no_symbols()
                print(f"{src}\t{dst}")


if __name__ == "__main__":
    main()

"""
実行結果

どこで	生れたか
見当が	つかぬ
所で	泣いて
ニャーニャー	泣いて
いた事だけは	記憶している
吾輩は	見た
ここで	始めて
ものを	見た
あとで	聞くと
我々を	捕えて
掌に	載せられて
スーと	持ち上げられた
時	フワフワした
感じが	あったばかりである
上で	落ちついて
顔を	見たのが
ものの	見始であろう
ものだと	思った
感じが	残っている
今でも	残っている
...

"""