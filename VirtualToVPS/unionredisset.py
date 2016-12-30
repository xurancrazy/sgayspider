import redis

rlocal = redis.StrictRedis(host='localhost', password='giligilisgay')


def unionkey(deskey, *sourcekeys):
    rlocal.sunionstore(deskey, *sourcekeys)
    if not rlocal.sismember("category", '"%s"' % deskey[9:]):
        rlocal.sadd("category", '"%s"' % deskey[9:])
    for sourcekey in sourcekeys:
        print("sourcekey = %s" % sourcekey)
        movies = rlocal.smembers(sourcekey)
        for movie in movies:
            moviekey = movie[1:-1].decode('utf-8')
            print("moviekey = %s" % moviekey)
            rlocal.srem("movieCategory:%s" % moviekey, '"%s"' % sourcekey[9:])
            print("rem = '%s'" % sourcekey[9:])
            rlocal.sadd("movieCategory:%s" % moviekey, '"%s"' % deskey[9:])
            print("add = '%s'" % deskey[9:])
        if sourcekey != deskey:
            rlocal.delete(sourcekey)
            rlocal.srem("category", '"%s"' % sourcekey[9:])

unionkey("category:恋爱", "category:恋爱", "category:恋爱戏剧", "category:恋爱接吻",
         "category:情侣", "category:Life", "category:Love", "category:初恋少女",
         "category:女儿","category:純真")
unionkey("category:受虐男", "category:受虐男", "category:受虐男接吻", "category:M男")
unionkey("category:姐妹", "category:姐妹", "category:スペレズ", "category:投稿姐妹",
         "category:女同","category:恋物癖女同")
unionkey("category:凌辱", "category:凌辱", "category:SM", "category:パニック",
         "category:折磨", "category:奴隶中女生","category:奴隶SM", "category:魔鬼系",
         "category:鬼イカセ", "category:大小姐调教", "category:鬼ピス","category:白人性奴",
         "category:真实","category:放尿","category:灌肠")
unionkey("category:戏剧", "category:戏剧", "category:戏剧温泉", "category:戏剧接吻",
         "category:婆婆戏剧","category:戏剧故事集", "category:戏剧出轨","category:故事集")
unionkey("category:角色扮演", "category:角色扮演", "category:动画人物")
unionkey("category:处男", "category:处男", "category:猥亵穿着处男", "category:戏剧处男")
unionkey("category:轮奸", "category:轮奸", "category:投稿轮奸")
unionkey("category:姐姐", "category:姐姐", "category:姐")
unionkey("category:屁股", "category:屁股", "category:大屁股", "category:美尻神",
         "category:感谢访问屁股")
unionkey("category:巨乳", "category:巨乳", "category:爆乳劇場", "category:超乳",
         "category:乳房","category:恋乳癖")
unionkey("category:熟女", "category:熟女", "category:婆婆接吻", "category:婆婆内衣",
         "category:婆婆出轨", "category:婆婆","category:母乳","category:白人","category:婆婆合集")
unionkey("category:少妇", "category:少妇","category:年轻妻子", "category:已婚妇女","category:寡妇")
unionkey("category:玩具", "category:玩具", "category:插入异物", "category:按摩棒",
         "category:触手","category:异物")
unionkey("category:女佣", "category:女佣", "category:家政妇", "category:车掌小姐","category:倒追")
unionkey("category:美少女", "category:美少女", "category:女大学生", "category:中女生",
         "category:女生","category:千金小姐","category:偶像", "category:GIRLS")
unionkey("category:露出", "category:露出", "category:露出调教","category:戏剧猥亵穿着",
         "category:猥亵穿着","category:短裤","category:脱衣")
unionkey("category:萝莉", "category:萝莉", "category:萝莉角色扮演","category:寄生妻")
unionkey("category:女教师", "category:女教师", "category:讲师","category:教学早泄","category:教学",
         "category:School")
unionkey("category:淫乱", "category:淫乱", "category:多P","category:OPEN",
         "category:SPECIAL", "category:Sex","category:Steel", "category:T-BACK",
         "category:すっぴん", "category:どM揉み","category:解禁","category:乱交","category:滥交",
         "category:粉丝感谢","category:女装人妖后宫","category:女装人妖")
unionkey("category:素人", "category:素人","category:业余", "category:明星脸")
unionkey("category:制服", "category:制服", "category:外套","category:校服","category:女检察官",
         "category:蓝光")
unionkey("category:乱伦", "category:乱伦", "category:禁断介護","category:伴侣")
unionkey("category:美腿", "category:美腿","category:恋腿癖", "category:足交")
unionkey("category:口交", "category:口交", "category:深喉","category:立即口交")
unionkey("category:隐退", "category:隐退", "category:引退")
unionkey("category:荡妇", "category:荡妇","category:淫语","category:复刻版",
         "category:10本番", "category:2016","category:女主人","category:DIGITAL",
         "category:DIVA", "category:Debut","category:E-BODY", "category:FUCK",
         "category:Hold","category:I", "category:Iku！", "category:者", "category:综合",
         "category:其他","category:/ハード", "category:女優", "category:アクション",
         "category:First","category:Impression", "category:新人","category:精选","category:胖女人",
         "category:汽车性爱",	"category:汽车","category:主观","category:原作合作",
         "category:首次亮相","category:介绍影片","category:原作合作", "category:MAXING",
         "category:MASOTRONIX", "category:More","category:New", "category:逢い引き",
         "category:白人温泉","category:COLLECTION", "category:BEST","category:BOX",
         "category:AV", "category:CLUB","category:3D", "category:3D！","category:感谢访问",
         "category:PREMIUM", "category:Present", "category:RQ着衣FUCK",
         "category:S1", "category:SOAP", "category:STYLISH", "category:TOHJIRO",
         "category:days","category:in", "category:teamZERO", "category:ω！",
         "category:排行榜","category:オジサマ",
         "category:ザ?面接", "category:ピタコス", "category:壊し愛","category:大好き。",
         "category:ゲーム実写版","category:パラダイスTV")
unionkey("category:痴女", "category:痴女","category:痴漢OK娘")
unionkey("category:流汗", "category:流汗","category:运动","category:接吻流汗")
unionkey("category:无码", "category:无码","category:下马")
unionkey("category:痴汉", "category:痴汉","category:痴汉电车")
unionkey("category:猎艳", "category:猎艳","category:摄影")
unionkey("category:强奸", "category:强奸","category:性骚扰","category:	烂醉如泥")
unionkey("category:乱醉如泥", "category:乱醉如泥","category:烂醉如泥")
