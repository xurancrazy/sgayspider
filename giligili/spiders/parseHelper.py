# -*- coding: utf-8 -*-
import logging

import redis

from giligili.items import TutorialItem

handler = logging.FileHandler('log/giligili.log')  # 实例化handler
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter
logger = logging.getLogger('giligili')  # 获取名为giligili的logger
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.ERROR)


r =redis.StrictRedis(host='localhost',port=6379,db=0)

baseUrl = r'http://www.nh87.cn'

def parseActorsListHelper(response):
    allActor = response.xpath('//*[@id="all"]/div')
    for actor in allActor:
        try:
            hrefUrl = actor.xpath('a/@href').extract()[0]
            targetUrl = '%s%s'%(baseUrl, hrefUrl)
            yield targetUrl
        except Exception as e:
            logger.error("Exception-->parseActorsListHelper:%s ,url = %s"%(e,response.url))

def parseActorHomeHelper(response):
    try:
        allYears = response.xpath('//*[@id="contrainer"]/div[1]/div[1]/div[2]/div/button')
        if len(allYears) == 0:
            yield response.url
        for year in allYears:
            hrefUrl = year.xpath('a/@href').extract()[0]
            targetUrl = '%s%s' % (baseUrl, hrefUrl)
            yield targetUrl
    except Exception as e:
        logger.error("Exception-->parseActorHomeHelper:%s ,url = %s" % (e,response.url))

def parseActorTargetYearHelper(response):
    allMovies = response.xpath('//*[@id="content"]/li')
    for movie in allMovies:
        try:
            item = TutorialItem()
            hrefUrl = movie.xpath('div/span[1]/a/@href').extract()[0]
            title = movie.xpath('div/span[2]/em/p/strong/text()').extract()[0]
            publishTime = movie.xpath('div/span[2]/div[2]/text()').extract()[0]
            item['url'] = '%s%s' % (baseUrl, hrefUrl)
            item['title'] = title
            item['publishTime'] = publishTime
            yield item
        except Exception as e:
            logger.error("Exception-->parseActorTargetYearHelper:%s , url = %s"%(e,response.url))

def parseContentHelper(response,item):
    try:
        item['fanhao'] = response.xpath('//*[@id="contrainer"]/div/h1/text()').extract()[0]
        item['avActor'] = response.xpath('//div[@class="weizhi2"]/a[2]/text()').extract()[0]
        item['classification'] = response.xpath('//div[@class="artCon"]/p').extract()[0]
        imgUrlList = response.xpath('//div[@class="artCon"]/img/@src').extract()
        if len(imgUrlList) == 0:
            imgUrlList = response.xpath('//div[@class="artCon"]/p[2]/img/@src').extract()
            if len(imgUrlList) == 0:
                imgUrl = response.xpath('//div[@class="artCon"]/div/img/@src').extract()[0]
            else:
                imgUrl = imgUrlList[0]
        else:
            imgUrl = imgUrlList[0]
        item['img'] = '%s%s' % (baseUrl, imgUrl)
        return item
    except Exception as e:
        logger.error("Exception-->parseContentHelper:%s ,url = %s" % (e, response.url))

