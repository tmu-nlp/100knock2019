#60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
import redis
from tqdm import tqdm

db = redis.StrictRedis(host='localhost', port=6379, db=0)

counter = 0
for  key in tqdm(db.scan_iter()):
    for erea in db.hvals(key):
        if erea == b'Japan':
            counter +=1

print(counter)


