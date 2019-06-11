import redis

r = redis.StrictRedis(host="localhost", port=6379, db=0)
keys = r.scan_iter()
count = 0
for key in keys:
    v = r.get(key).decode("utf-8")
    if v == "Japan":
        count += 1
print(count)
#22128