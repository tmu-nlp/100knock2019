import redis

r = redis.StrictRedis(host="localhost", port=6379, db=0)
v = r.get("The Wanderers").decode("utf-8")
print(v)
#United States