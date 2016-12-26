import redis


rlocal = redis.StrictRedis(host='118.184.28.172',password='giligilisgay')
rvirtualmachine = redis.StrictRedis(host='localhost')
keys = rvirtualmachine.smembers('classification')
print(keys)
for key in keys:
    nowkey = key.decode('utf-8')
    nowkey1 = '"%s"'%nowkey
    print(nowkey1)
    rlocal.sadd('category',nowkey1)
    values = rvirtualmachine.smembers('classification:%s' % nowkey)
    print(values)
    for value in values:
        nowvalue = value.decode('utf-8').strip()
        nowvalue1 = '"%s"'%nowvalue
        rlocal.sadd('category:%s'%nowkey,nowvalue1)
