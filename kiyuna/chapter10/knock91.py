'''
91. アナロジーデータの準備
単語アナロジーの評価データをダウンロードせよ．
このデータ中で": "で始まる行はセクション名を表す．
例えば，": capital-common-countries"という行は，
"capital-common-countries"というセクションの開始を表している．
ダウンロードした評価データの中で，
"family"というセクションに含まれる評価事例を抜き出してファイルに保存せよ．
'''
in_path = 'questions-words.txt'
out_path = 'out91.txt'
with open(out_path, 'w') as f_out:
    capturing = False
    for line in map(lambda x: x.rstrip(), open(in_path)):
        if line[0] == ':':
            capturing = line == ': family'
        elif capturing:
            print(line, file=f_out)
