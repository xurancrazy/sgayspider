import redis

r =redis.StrictRedis(host='localhost',port=6379,db=0)
for i in r.smembers("url:crawled"):
    print(i)