# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql


class LbwscrapyPipeline(object):
    def __init__(self):
        # 连接数据库
        self.conn = None
        # 游标
        self.cur = None

    # 打开爬虫时调用，只调用一次
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            user="meituan_cate",
            password="54dsWWPnGMyhdKzH",
            host="114.116.126.177",
            port=6653,
            database="meituan_cate",
            charset="utf8"
        )

        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            if item["phone"]:
                clos, value = zip(*item.items())
                # print(value)
                query_sql = f"""select * from lbw_store where  phone='{item["phone"]}' """
                # print('sql语句', query_sql, value)

                # 如果字段已存在就不执行sql
                if not self.cur.execute(query_sql):
                    sql = "INSERT INTO %s(%s) VALUES (%s)" % ('lbw_store', ','.join(clos), ','.join(['%s'] * len(value)))
                    self.cur.execute(sql, value)
                    self.conn.commit()

                return item
            else:
                return item
        except Exception as e:
            print(e)

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
