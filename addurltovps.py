import redis

rremote = redis.StrictRedis(host='118.184.28.172',password='giligilisgay')
rvirtualmachine = redis.StrictRedis(host='localhost')

keys = rvirtualmachine.smembers('url')
for key in keys:
    print('nowkey = %s' % key)
    rremote.sadd('url',key)

