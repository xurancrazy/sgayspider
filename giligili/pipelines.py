# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

logger = logging.getLogger()
class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class CustomImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url = item['img']
        return scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['img_filepath'] = image_paths[0].split('/')[1]
        return item

class MySQLStoreGiliGiliPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool
    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            port=3306,
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USERNAME'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode= True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    #pipeline默认调用
    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self.upOrInsert, item, spider)
        d.addErrback(self.handleError, item, spider)
        return d

    #将每行更新或写入数据库中
    def upOrInsert(self, conn, item, spider):
        fanhao = item['fanhao'].decode("utf-8")
        teacher = item['avActor'].decode("utf-8")
        title = item['title'].decode("utf-8")
        publishTime = item['publishTime'].decode("utf-8")
        imgHref = item['img'].decode("utf-8")
        img_filepath = item['img_filepath']
        s = 'select * from movies where fanhao = \'%s\''%(fanhao)
        conn.execute(s)
        ret = conn.fetchone()
        if ret:
            if img_filepath:
                s = 'update movies set imgHref = \'%s\' where fanhao = \'%s\''%(img_filepath,fanhao)
                conn.execute(s)
                logger.info("%s exists in movies"%fanhao)
        else:
            #insert movies table
            logger.info("begin insert database")
            s ='insert into movies (fanhao, title, teacher, publishTime, imgHref) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'%(fanhao, title, teacher, publishTime,img_filepath if img_filepath else imgHref)
            conn.execute(s)
            #insert teachers table
            s = 'select * from teachers where name = \'%s\''%(teacher)
            conn.execute(s)
            ret = conn.fetchone()
            if ret:
                s = 'update teachers set moviesNum=moviesNum+1 where name = \'%s\''%(teacher)
                conn.execute(s)
            else:
                s = 'insert into teachers(name) VALUES (\'%s\')'%(teacher)
                conn.execute(s)

    def handleError(self,failure, item, spider):
        logger.error("database execute error")