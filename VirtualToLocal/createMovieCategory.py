import redis

rlocal = redis.StrictRedis(host='192.168.1.104',password='giligili')

keys = rlocal.smembers('category')
for key in keys:
    realkey = key.decode('utf-8')
    print('realkey = %s' % realkey)
    movies = rlocal.smembers('category:%s'%key[1:-1].decode('utf-8'))
    for movie in movies:
        realmovie = movie[1:-1].decode('utf-8').strip()
        print('realmovie = %s'%realmovie)
        rlocal.sadd('movieCategory:%s'%realmovie,realkey)
