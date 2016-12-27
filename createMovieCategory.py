import redis

rvirtual = redis.StrictRedis(host='localhost')

keys = rvirtual.smembers('category')
for key in keys:
    realkey = key.decode('utf-8')
    print('realkey = %s' % realkey)
    movies = rvirtual.smembers('category:%s'%key[1:-1].decode('utf-8'))
    for movie in movies:
        realmovie = movie[1:-1].decode('utf-8').strip()
        print('realmovie = %s'%realmovie)
        rvirtual.sadd('movieCategory:%s'%realmovie,realkey)
