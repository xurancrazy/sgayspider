import redis

rlocal = redis.StrictRedis(host='192.168.1.104',password='giligili')
rvirtualmachine = redis.StrictRedis(host='localhost')

keys = rvirtualmachine.smembers('classification')
for key in keys:
    nowkey = key.decode('utf-8')
    nowkey1 = '"%s"'%nowkey
    print('nowkey = %s'%nowkey)
    print('nowkey1 = %s'%nowkey1)
    values = rvirtualmachine.smembers('classification:%s'%nowkey)
    print('values in key:%s  --> %s'%(nowkey,values))
    for value in values:
        nowvalue = value.decode('utf-8').strip()
        print('nowvalue = %s'%nowvalue)
        rlocal.sadd('movieCategory:%s'%nowvalue,nowkey1)
