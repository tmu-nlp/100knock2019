import redis
'''
$ brew install redis
$ redis-server /usr/local/etc/redis.conf
'''

redis_db = redis.Redis(host='localhost', port=6379, db=0)

print(redis_db.hgetall("SMAP"))
# b'Japan'
print(redis_db.hgetall("Justin Bieber"))
# b'Canada'
print(redis_db.hgetall("Ed Sheeran"))
# b'United Kingdom'