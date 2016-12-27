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

unionkey("category:女生", "category:女生", "category:GIRLS")
unionkey("category:恋爱", "category:恋爱", "category:恋爱戏剧", "category:恋爱接吻",
         "category:情侣", "category:Life", "category:Love", "category:初恋少女",
         "category:女儿","category:純真")
unionkey("category:受虐男", "category:受虐男", "category:受虐男接吻", "category:M男")
unionkey("category:姐妹", "category:姐妹", "category:スペレズ", "category:投稿姐妹",
         "category:女同")
unionkey("category:凌辱", "category:凌辱", "category:SM", "category:パニック",
         "category:折磨", "category:奴隶中女生","category:奴隶SM", "category:魔鬼系",
         "category:鬼イカセ", "category:大小姐调教", "category:鬼ピス","category:白人性奴",
         "category:真实","category:放尿","category:灌肠")
unionkey("category:DIGITAL", "category:DIGITAL", "category:オジサマ",
         "category:ザ?面接", "category:ピタコス", "category:壊し愛","category:大好き。")
unionkey("category:戏剧", "category:戏剧", "category:戏剧温泉", "category:戏剧接吻",
         "category:婆婆戏剧","category:戏剧故事集", "category:戏剧出轨","category:故事集")
unionkey("category:角色扮演", "category:角色扮演", "category:动画人物")
unionkey("category:处男", "category:处男", "category:猥亵穿着处男", "category:戏剧处男")
unionkey("category:轮奸", "category:轮奸", "category:投稿轮奸")
unionkey("category:姐姐", "category:姐姐", "category:姐")
unionkey("category:屁股", "category:屁股", "category:大屁股", "category:美尻神")
unionkey("category:巨乳", "category:巨乳", "category:爆乳劇場", "category:超乳",
         "category:乳房","category:恋乳癖")
unionkey("category:熟女", "category:熟女", "category:婆婆接吻", "category:婆婆内衣",
         "category:婆婆出轨", "category:婆婆","category:母乳","category:白人")
unionkey("category:少妇", "category:年轻妻子", "category:已婚妇女","category:寡妇")
unionkey("category:玩具", "category:玩具", "category:插入异物", "category:按摩棒",
         "category:触手","category:异物")
unionkey("category:女佣", "category:女佣", "category:家政妇", "category:车掌小姐","category:倒追")
unionkey("category:美少女", "category:美少女", "category:女大学生", "category:中女生",
         "category:女生","category:千金小姐","category:偶像")
unionkey("category:露出", "category:露出", "category:露出调教","category:戏剧猥亵穿着","category:猥亵穿着",
         "category:短裤","category:脱衣")
unionkey("category:萝莉", "category:萝莉", "category:萝莉角色扮演","category:寄生妻")
unionkey("category:女教师", "category:女教师", "category:讲师","category:教学早泄","category:教学",
         "category:School")
unionkey("category:淫乱", "category:淫乱", "category:多P","category:OPEN",
         "category:SPECIAL", "category:Sex","category:Steel", "category:T-BACK",
         "category:すっぴん", "category:どM揉み","category:解禁","category:乱交","category:滥交",
         "category:粉丝感谢")
unionkey("category:素人", "category:素人","category:业余", "category:明星脸")
unionkey("category:制服", "category:制服", "category:外套","category:校服",	"category:女检察官")
unionkey("category:乱伦", "category:乱伦", "category:禁断介護","category:伴侣")
unionkey("category:美腿", "category:恋腿癖", "category:足交")
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
         "category:排行榜")
unionkey("category:痴女", "category:痴女","category:痴漢OK娘")
unionkey("category:流汗", "category:流汗","category:运动")
unionkey("category:无码", "category:无码","category:下马")
unionkey("category:痴汉", "category:痴汉","category:痴汉电车")
unionkey("category:猎艳", "category:猎艳","category:摄影")
unionkey("category:强奸", "category:强奸","category:性骚扰")
# rlocal.sunionstore("category:3D","category:3D","category:3D！")
# rlocal.delete("category:3D！")
# rlocal.srem("category",'"3D！"')

# rlocal.sunionstore("category:COLLECTION","category:COLLECTION","category:BEST",
#                    "category:BOX","category:AV","category:CLUB")
# rlocal.delete("category:BEST")
# rlocal.delete("category:BOX")
# rlocal.delete("category:AV")
# rlocal.delete("category:CLUB")
# rlocal.srem("category",'"BEST"')
# rlocal.srem("category",'"BOX"')
# rlocal.srem("category",'"AV"')
# rlocal.srem("category",'"CLUB"')
# rlocal.sunionstore("category:10本番","category:10本番","category:2016")
# rlocal.delete("category:2016")
# rlocal.srem("category",'"2016"')
# rlocal.sunionstore("category:DIGITAL","category:DIGITAL","category:DIVA","category:Debut",
#                    "category:E-BODY","category:FUCK","category:Hold",
#                    "category:I","category:Iku！")
# rlocal.delete("category:DIVA")
# rlocal.delete("category:Debut")
# rlocal.delete("category:E-BODY")
# rlocal.delete("category:FUCK")
# rlocal.delete("category:Hold")
# rlocal.delete("category:I")
# rlocal.delete("category:Iku！")
# rlocal.srem("category",'"DIVA"')
# rlocal.srem("category",'"Debut"')
# rlocal.srem("category",'"E-BODY"')
# rlocal.srem("category",'"FUCK"')
# rlocal.srem("category",'"Hold"')
# rlocal.srem("category",'"I"')
# rlocal.srem("category",'"Iku！"')
# rlocal.sunionstore("category:First Impression","category:First Impression","category:First","category:Impression")
# rlocal.sadd("category",'"First Impression"')
# rlocal.delete("category:First")
# rlocal.delete("category:Impression")
# rlocal.srem("category",'"First"')
# rlocal.srem("category",'"Impression"')
# rlocal.sunionstore("category:女生","category:女生","category:GIRLS")
# rlocal.delete("category:GIRLS")
# rlocal.srem("category",'"GIRLS"')
# rlocal.sunionstore("category:恋爱","category:恋爱","category:恋爱戏剧","category:恋爱接吻",
#                    "category:情侣","category:Life","category:Love")
# rlocal.delete("category:恋爱戏剧")
# rlocal.delete("category:恋爱接吻")
# rlocal.delete("category:情侣")
# rlocal.delete("category:Life")
# rlocal.delete("category:Love")
# rlocal.srem("category",'"恋爱戏剧"')
# rlocal.srem("category",'"恋爱接吻"')
# rlocal.srem("category",'"情侣"')
# rlocal.srem("category",'"Life"')
# rlocal.srem("category",'"Love"')
# rlocal.sunionstore("category:MAXING","category:MAXING","category:MASOTRONIX","category:More",
#                    "category:New")
# rlocal.delete("category:MASOTRONIX")
# rlocal.delete("category:More")
# rlocal.delete("category:New")
# rlocal.srem("category",'"MASOTRONIX"')
# rlocal.srem("category",'"More"')
# rlocal.srem("category",'"New"')
# rlocal.sunionstore("category:PREMIUM","category:PREMIUM","category:Present","category:RQ着衣FUCK",
#                    "category:S1","category:SOAP","category:STYLISH","category:TOHJIRO","category:days",
#                    "category:in","category:teamZERO","category:ω！")
# rlocal.delete("category:Present")
# rlocal.delete("category:RQ着衣FUCK")
# rlocal.delete("category:S1")
# rlocal.delete("category:SOAP")
# rlocal.delete("category:STYLISH")
# rlocal.delete("category:TOHJIRO")
# rlocal.delete("category:days")
# rlocal.delete("category:in")
# rlocal.delete("category:teamZERO")
# rlocal.delete("category:ω！")
# rlocal.srem("category",'"Present"')
# rlocal.srem("category",'"RQ着衣FUCK"')
# rlocal.srem("category",'"S1"')
# rlocal.srem("category",'"SOAP"')
# rlocal.srem("category",'"STYLISH"')
# rlocal.srem("category",'"TOHJIRO"')
# rlocal.srem("category",'"days"')
# rlocal.srem("category",'"in"')
# rlocal.srem("category",'"teamZERO"')
# rlocal.srem("category",'"ω！"')
# rlocal.sunionstore("category:受虐男","category:受虐男","category:受虐男接吻","category:M男")
# rlocal.delete("category:受虐男接吻")
# rlocal.delete("category:M男")
# rlocal.srem("category",'"受虐男接吻"')
# rlocal.srem("category",'"M男"')
# rlocal.sunionstore("category:OPEN","category:OPEN","category:SPECIAL","category:Sex",
#                    "category:Steel","category:T-BACK","category:すっぴん","category:どM揉み")
# rlocal.delete("category:SPECIAL")
# rlocal.delete("category:Sex")
# rlocal.delete("category:Steel")
# rlocal.delete("category:T-BACK")
# rlocal.delete("category:すっぴん")
# rlocal.delete("category:どM揉み")
# rlocal.srem("category",'"SPECIAL"')
# rlocal.srem("category",'"Sex"')
# rlocal.srem("category",'"Steel"')
# rlocal.srem("category",'"T-BACK"')
# rlocal.srem("category",'"すっぴん"')
# rlocal.srem("category",'"どM揉み"')
# rlocal.sunionstore("category:姐妹","category:姐妹","category:スペレズ")
# rlocal.delete("category:スペレズ")
# rlocal.srem("category",'"スペレズ"')
# rlocal.sunionstore("category:SM","category:SM","category:パニック")
# rlocal.delete("category:パニック")
# rlocal.srem("category",'"パニック"')
# rlocal.sunionstore("category:DIGITAL","category:DIGITAL","category:オジサマ",
#                    "category:ザ?面接","category:ピタコス")
# rlocal.delete("category:オジサマ")
# rlocal.delete("category:ザ?面接")
# rlocal.delete("category:ピタコス")
# rlocal.srem("category",'"オジサマ"')
# rlocal.srem("category",'"ザ?面接"')
# rlocal.srem("category",'"ピタコス"')
