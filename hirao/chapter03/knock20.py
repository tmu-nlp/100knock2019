import gzip
import json


def get_json(country="イギリス"):
    with gzip.open('jawiki-country.json.gz') as files:
        for f in files:
            data_json = json.loads(f)
            if data_json["title"] == country:
                break
    return (data_json["text"])


print(get_json())
