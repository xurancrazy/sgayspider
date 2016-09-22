from giligili.items import TutorialItem

baseUrl = r'http://www.nh87.cn'

def parseActorsListHelper(response):
    allActor = response.xpath('//*[@id="all"]/div')
    for actor in allActor:
        hrefUrl = actor.xpath('a/@href').extract()[0]
        targetUrl = '%s%s'%(baseUrl, hrefUrl)
        yield targetUrl

def parseActorHomeHelper(response):
    allYears = response.xpath('//*[@id="contrainer"]/div[1]/div[1]/div[2]/div/button')
    for year in allYears:
        hrefUrl = year.xpath('a/@href').extract()[0]
        targetUrl = '%s%s' % (baseUrl, hrefUrl)
        yield targetUrl

def parseActorTargetYearHelper(response):
    allMovies = response.xpath('//*[@id="content"]/li')
    for movie in allMovies:
        item = TutorialItem()
        hrefUrl = movie.xpath('div/span[1]/a/@href').extract()[0]
        title = movie.xpath('div/span[2]/em/p/strong/text()').extract()[0].encode('utf-8')
        publishTime = movie.xpath('div/span[2]/div[2]/text()').extract()[0]
        item['url'] = '%s%s' % (baseUrl, hrefUrl)
        item['title'] = title
        item['publishTime'] = publishTime
        yield item

def parseContentHelper(response,item):
    item['fanhao'] = response.xpath('//*[@id="contrainer"]/div/h1/text()').extract()[0]
    item['avActor'] = response.xpath('//*[@id="contrainer"]/div/div[1]/p/span[2]/a/text()').extract()[0].encode('utf-8')
    imgUrl = response.xpath('//div[@class="artCon"]/img/@src').extract()[0]
    item['img'] = '%s%s' % (baseUrl, imgUrl)
    return item