import gzip
import json
import redis
from tqdm import tqdm_notebook as tqdm
import re
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
        count = len(data_json.get("tags", ""))
        redis_db.hset(name, "tag_num", count)
        if count > 0:
            tags = [x["value"] for x in data_json["tags"]]
            redis_db.hset(name, "tags", "\t".join(tags))
print(f"{redis_db.dbsize()}件登録")

def get_tags(name):
    tag_num = int(re.sub("b|'", "", str(redis_db.hgetall(name).get(b'tag_num', 0))))
    output = f"{name} has {tag_num}tags"
    if tag_num > 0:
        tags = re.sub("b|'", "", str(redis_db.hgetall(name).get(b'tags', "")))
        output += f"\n{tags}"
    print(output)

get_tags("Taylor Swift")
get_tags("Justin Bieber")
'''
Justin Bieber has 5tags
gay teen pop lack metal pop amazing
Taylor Swift has 7tags
taylor-swift country pop fixme lael mess country-pop top 40 female vocals
'''
