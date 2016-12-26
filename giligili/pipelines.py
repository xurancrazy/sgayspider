# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors
from giligili.spiders.parseHelper import logger
from giligili.spiders.parseHelper import r

class CustomImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url = item['img']
        if image_url:
            return scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            item['img_filepath'] = ''
            logger.error("Item contains no images,imgurl = %s , url = %s"%(item['img'],item['url']))
        else:
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
            cursorclass = pymysql.cursors.DictCursor,
            use_unicode= True,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbargs)
        return cls(dbpool)

    #pipeline默认调用
    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self.upOrInsert, item, spider)
        d.addErrback(self.handleError, item)
        return d

    #将每行更新或写入数据库中
    def upOrInsert(self, conn, item, spider):
        fanhao = item['fanhao']
        teacher = item['avActor']
        title = item['title']
        publishTime = item['publishTime']
        imgHref = item['img']
        img_filepath = item['img_filepath']
        classification = item['classification']

        s = 'select * from movies where fanhao = \'%s\''%(fanhao)
        conn.execute(s)
        ret = conn.fetchone()
        if ret:
            if img_filepath:
                s = 'update movies set imgHref = \'%s\' where fanhao = \'%s\''%(img_filepath,fanhao)
                conn.execute(s)
                logger.debug("%s exists in movies"%(fanhao))
                r.sadd('urlfortest', item['url'])
                self.regex(r, item)
        else:
            #insert movies table
            logger.debug("begin insert movies table,fanhao = %s"%(fanhao))
            s ='insert into movies (fanhao, title, teacher, publishTime, imgHref) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'%(fanhao, title, teacher, publishTime,img_filepath if img_filepath else imgHref)
            conn.execute(s)
            logger.debug("complete insert movies table,fanhao = %s" % (fanhao))
            logger.debug("begin query teachers table,fanhao = %s" % (fanhao))
            #insert teachers table
            s = 'select * from teachers where name = \'%s\''%(teacher)
            conn.execute(s)
            ret = conn.fetchone()
            if ret:
                logger.debug("begin update teachers table,fanhao = %s" % (fanhao))
                s = 'update teachers set moviesNum=moviesNum+1 where name = \'%s\''%(teacher)
                conn.execute(s)
                logger.debug("complete update teachers table,fanhao = %s" % (fanhao))
            else:
                logger.debug("begin insert teachers table,fanhao = %s" % (fanhao))
                s = 'insert into teachers(name) VALUES (\'%s\')'%(teacher)
                conn.execute(s)
                logger.debug("complete insert teachers table,fanhao = %s" % (fanhao))
            r.sadd('urlfortest',item['url'])
            self.regex(r,item)

    def handleError(self,failure, item):
        logger.error("database execute error,fanhao = %s"%(item['fanhao']))
        logger.error(failure)

    def regex(self,r,item):
        classification = item['classification']
        res = re.search('定义于：.*正式发片', classification, flags=0)
        if not res.group():
            return
        pre = res.group(0)
        pre2 = pre[4:-5]
        logger.debug("fanhao:%s , classification:%s" % (item['fanhao'],classification))
        matrix = pre2.split("、")
        length = len(matrix)
        if length == 0:
            return
        self.saveclassfication(r,matrix,length,item)

    def saveclassfication(self,r,matrix,length,item):
        logger.debug("start saveclassfication")
        for i in range(length):
            s= matrix[i].strip()
            if len(s)==0:
                continue
            r.sadd('category',"%s"%(s.decode('utf-8')))
            r.sadd(('category:%s'%s),item['fanhao'])
