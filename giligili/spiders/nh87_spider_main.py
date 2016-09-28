
import scrapy
from giligili.spiders.parseHelper import *

class giligiliSpider_Main(scrapy.Spider):
    name = "giligili"
    start_urls = [
        "http://www.nh87.cn/find.html"
    ]

    def parse(self, response):
        for url in parseActorsListHelper(response):
            yield scrapy.Request(url, callback=self.parseActorHome,errback=self.handleError)

    def parseActorHome(self, response):
        for url in parseActorHomeHelper(response):
            yield scrapy.Request(url, callback=self.parseActorTargetYear,errback=self.handleError)

    def parseActorTargetYear(self, response):
        for item in parseActorTargetYearHelper(response):
            url = item['url']
            if r.sismember('url:crawled',url):
                logger.debug("url = %s,already be scraped"%(url))
                continue
            yield scrapy.Request(url, meta={'item': item}, callback=self.parseContent,errback=self.handleError)

    def parseContent(self, response):
        item = response.meta['item']
        return parseContentHelper(response, item)

    def handleError(self,failure):
        logger.error("HTTP Error-->%s"%(repr(failure)))