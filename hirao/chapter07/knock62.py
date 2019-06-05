import redis
from tqdm import tqdm_notebook as tqdm
redis_db = redis.Redis(host='localhost', port=6379, db=0)

# フルスキャン
count = 0
for i, key in enumerate(tqdm(redis_db.scan_iter())):
    #　HashesのValue取得
    for area in redis_db.hvals(key):
        if area == b'Japan':
            count += 1
print(count)
# 22821