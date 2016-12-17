from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors

def formatdatetime(date):
    res = ""


def formatdata():
    dbargs = dict(
        host='localhost',
        port=3306,
        db='giligiliforspider',
        user='root',
        passwd='xuran',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
        use_unicode=True,
    )
    dbpool = adbapi.ConnectionPool('pymysql', **dbargs)
    conn = dbpool.connect()
    # s = 'select * from movies where teacher = \'%s\''%('泷泽萝拉')
    s = 'select * from movies'
    cursor = conn.cursor()
    cursor.execute(s)
    list = cursor.fetchall()
    try:
        for row in list:
            fanhao=row['fanhao']
            res = row['publishTime'].strip()
            res1=res.replace('年','-')
            res2=res1.replace('月', '-')
            res3=res2.replace('日', '')
            res4=res3.replace('/', '-')
            if res4=='240':
                res4='2016-11-07'
            list=res4.split('-')
            if len(list[1])<2:
                list[1]='0'+list[1]
            if len(list[2])<2:
                list[2]='0'+list[2]
            res5='-'.join(list)
            s='update movies set publishTime = \'%s\' where fanhao = \'%s\''%(res5,fanhao)
            cursor.execute(s)
            conn.commit()
            print(res5)
    except Exception as e:
        print(row)

    conn.close()

formatdata()