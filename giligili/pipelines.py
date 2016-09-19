# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

logger = logging.getLogger()
class TutorialPipeline(object):
    def process_item(self, item, spider):
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

        s = 'select * from movies where fanhao = \'%s\''%(fanhao)
        conn.execute(s)
        ret = conn.fetchone()
        if ret:
            logger.info("%s exists in movies"%fanhao)
        else:
            #insert movies table
            logger.info("begin insert database")
            s ='insert into movies (fanhao, title, teacher, publishTime, imgHref) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'%(fanhao, title, teacher, publishTime,imgHref)
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
        logger.error("errorOn->",item['fanhao'].decode("utf-8"))