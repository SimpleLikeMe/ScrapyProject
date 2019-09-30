# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from .settings import *


class AlibabascrapyPipeline(object):
    def __init__(self):
        # 连接数据库
        self.conn = None
        # 游标
        self.cur = None

    # 打开爬虫时调用，只调用一次
    def open_spider(self, spider):
        self.conn = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST, port=MYSQL_PORT,
                                    database=MYSQL_DB, charset="utf8"
                                    )

        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            print(item["phone"])
            if item["phone"]:
                clos, value = zip(*item.items())
                query_sql = f"""select phone from {MYSQL_TABLE} where  phone='{item["phone"]}' """
                print(query_sql)
                # 如果字段已存在就不执行sql
                if not self.cur.execute(query_sql):
                    sql = "INSERT INTO %s(%s) VALUES (%s)" % (
                        MYSQL_TABLE, ','.join(clos), ','.join(['%s'] * len(value)))
                    print(sql)
                    self.cur.execute(sql, value)
                    self.conn.commit()
                print("end")
                return item
            else:
                return item
        except Exception as e:
            print(e)

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
