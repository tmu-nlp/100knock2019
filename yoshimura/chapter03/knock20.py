'''
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，
「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
'''
import gzip
import json

with gzip.open('jawiki-country.json.gz', 'rt', encoding='utf-8') as fr, \
     open('Briten.txt', 'w', encoding='utf-8') as fw:
    for line in fr:
        json_dict = json.loads(line)
        if json_dict['title'] == 'イギリス':
            fw.write(json_dict['text'])
            break
