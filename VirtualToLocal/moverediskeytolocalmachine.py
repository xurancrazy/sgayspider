import redis


rlocal = redis.StrictRedis(host='192.168.1.104',password='giligili')
rvirtualmachine = redis.StrictRedis(host='localhost')

rvirtualcategorykeys = rvirtualmachine.smembers('category')
for rvirtualcategorykey in rvirtualcategorykeys:
    realkey = rvirtualcategorykey.decode('utf-8')
    print("realkey=%s"%realkey)
    rlocal.sadd('category',realkey)
    values = rvirtualmachine.smembers('category:%s' % rvirtualcategorykey[1:-1].decode('utf-8'))
    for value in values:
        nowvalue = value.decode('utf-8').strip()
        print("nowvalue=%s" % nowvalue)
        rlocal.sadd('category:%s'%rvirtualcategorykey[1:-1].decode('utf-8'),nowvalue)
