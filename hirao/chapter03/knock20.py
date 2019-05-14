import gzip
import json

FILE_PATH = 'jawiki-country.json.gz'

# 関数get_textを宣言する
def get_text(country="イギリス"):
    with gzip.open(FILE_PATH) as files:
        # 複数の国のデータがあるので、該当する国を探索する
        for f in files:
            data_json = json.loads(f)
            if data_json["title"] == country:
                break
    return (data_json["text"])

print(get_text())