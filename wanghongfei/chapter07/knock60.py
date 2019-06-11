import redis
import json

r = redis.StrictRedis(host="localhost", port=6379, db=0)
r.flushdb()
with open("/users/hongfeiwang/100knock2019/wanghongfei/chapter07/artist.json", "r") as f:
    for line in f:
        data = json.loads(line)
        if "area" in data:
            r.set(data["name"], data["area"])
r.save()