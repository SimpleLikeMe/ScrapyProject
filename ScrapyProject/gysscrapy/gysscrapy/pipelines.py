import pymysql


class GysscrapyPipeline(object):
    def __init__(self):
        # 连接数据库
        self.conn = None
        # 游标
        self.cur = None

    # 打开爬虫时调用，只调用一次
    def open_spider(self, spider):
        self.conn = pymysql.connect(host='127.0.0.1',
                                    user='root',
                                    password="jiefutong",
                                    database='crawl',
                                    port=3306,
                                    charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        clos, value = zip(*item.items())

        query_sql = f"""select * from gys where  name='{value[0]}'
        and phone='{value[2]}' """
        # print('sql语句', query_sql, value)
        # sql = "INSERT INTO %s(%s) VALUES (%s)" % ('gys', ','.join(clos), ','.join(['%s'] * len(value)))
        # print('sql语句', sql, value)
        # 如果字段已存在就不执行sql
        if not self.cur.execute(query_sql):
            sql = "INSERT INTO %s(%s) VALUES (%s)" % ('gys', ','.join(clos), ','.join(['%s'] * len(value)))
            self.cur.execute(sql, value)
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
