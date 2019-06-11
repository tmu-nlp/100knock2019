import redis
import json

r = redis.StrictRedis(host="localhost", port=6379, db=1)
r.flushdb()
with open("/users/hongfeiwang/100knock2019/wanghongfei/chapter07/artist.json", "r") as f:
    for line in f:
        data = json.loads(line)
        if "tags" in data:
            r.set(data["name"], str(data["tags"]))
r.save()

name = "Sir Adrian"
v = r.get(name).decode("utf-8")
print(v)
