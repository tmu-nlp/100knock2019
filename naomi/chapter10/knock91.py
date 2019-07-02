# 91. アナロジーデータの準備
# 単語アナロジーの評価データをダウンロードせよ．このデータ中で": "で始まる行はセクション名を表す．
# 例えば，": capital-common-countries"という行は，"capital-common-countries"
# というセクションの開始を表している．
# ダウンロードした評価データの中で，"family"というセクションに含まれる評価事例を抜き出してファイルに保存せよ．

with open('family.txt', 'w+', encoding='utf-8') as f:
    
    for line in open('questions-words.txt', 'r', encoding='utf-8').readlines():
        if line.startswith(': ') and not line.startswith(': family'):
            keep = False
        elif line.startswith(': family'):
            keep = True
        elif keep is True:
            print(line.rstrip(), file=f)
