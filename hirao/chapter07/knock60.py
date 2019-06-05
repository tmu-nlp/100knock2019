import gzip
import json
import redis
from tqdm import tqdm_notebook as tqdm
'''
$ brew install redis
$ redis-server /usr/local/etc/redis.conf
'''

redis_db = redis.Redis(host='localhost', port=6379, db=0)

file_name = "artist.json.gz"

with gzip.open(file_name) as data_file:
    # 01:47
    for line in tqdm(data_file):
        data_json = json.loads(line)
        name = data_json["name"]
        artist_id = data_json["id"]
        value = data_json.get("area", "")
        redis_db.hset(name, artist_id, value)
print(f"{redis_db.dbsize()}件登録")