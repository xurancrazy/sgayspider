import scrapy
from parseHelper import *

class giligiliSpider_Main(scrapy.Spider):
    name = "giligili"
    start_urls = [
        "http://www.nh87.cn/find.html"
    ]

    def parse(self, response):
        for url in parseActorsListHelper(response):
            yield scrapy.Request(url, callback=self.parseActorHome)

    def parseActorHome(self, response):
        for url in parseActorHomeHelper(response):
            yield scrapy.Request(url, callback=self.parseActorTargetYear)

    def parseActorTargetYear(self, response):
        for item in parseActorTargetYearHelper(response):
            url = item['url']
            yield scrapy.Request(url, meta={'item': item}, callback=self.parseContent)

    def parseContent(self, response):
        item = response.meta['item']
        return parseContentHelper(response, item)
