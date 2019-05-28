'''
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

返事をする      と に は        及ばんさと 手紙に 主人は
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語（サ変接続名詞+を+動詞）
コーパス中で頻出する述語と助詞パターン
'''
from operator import itemgetter
from knock41 import get_chunk_list

for chunks in get_chunk_list("neko.txt.cabocha"):
    for chunk in chunks:
        if not chunk.check_pos('動詞'):
            continue

        # 係り元の「サ変接続名詞+を（助詞）」で構成される文節を取得
        sahen_wo = ''
        for src in chunk.srcs:
            sahen_wo = chunks[src].get_sahen_wo()

        if not sahen_wo:
            continue

        predicate = sahen_wo + chunk.get_surfaces('pos', '動詞')[0]  # 述語
        case_frame = []
        for src in chunk.srcs:
            if len(chunks[src].get_surfaces('pos', '助詞')) == 0:
                continue
            case = chunks[src].get_surfaces('pos', '助詞').pop()
            if case != "を":
                case_frame.append((
                    case,  # 格パターン
                    chunks[src].normalized_surface()  # 項（文節そのもの）
                ))

        if case_frame:
            case_frame.sort(key=itemgetter(0))
            print(f"{predicate}\t \
                    {' '.join([x[0] for x in case_frame])}\t \
                    {' '.join([x[1] for x in case_frame])}")