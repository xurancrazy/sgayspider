import redis

r = redis.StrictRedis(host='localhost',password='giligilispider')

keys = r.smembers("category")
for key in keys:
    realkey = "category:%s"%(key[1:-1].decode('utf-8'))
    print("realkey=%s"%realkey)
    movies = r.smembers(realkey)
    for movie in movies:
        realmovie=movie.decode('utf-8')
        if realmovie[0]!='"':
            print(realmovie)
            r.sadd(realkey,'"%s"'%realmovie)
            r.srem(realkey,realmovie)
