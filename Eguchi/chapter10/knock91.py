"""
単語アナロジーの評価データをダウンロードせよ．このデータ中で": "で始まる行はセクション名を表す．
例えば，": capital-common-countries"という行は，"capital-common-countries"というセクションの開始を表している．
ダウンロードした評価データの中で，"family"というセクションに含まれる評価事例を抜き出してファイルに保存せよ．
"""

in_f = "questions-words.txt"
out_f = "family.txt"

with open(in_f, "rt") as in_data, open(out_f, "wt") as out_data:
    
    dis = False
    
    for line in  in_data:
        if dis == True:
            if line.startswith(": "):
                break
            #print(line.strip(), file=out_f)
            print(line.strip(), file=out_data)
        
        elif line.startswith(": family"):
            print("yes")
            dis = True
            