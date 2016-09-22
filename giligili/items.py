# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fanhao = scrapy.Field()
    avActor = scrapy.Field()
    publishTime = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    img = scrapy.Field() #nh87's img url
    img_result = scrapy.Field() #save request result for nh87's img url
    img_filepath = scrapy.Field() #native's img url