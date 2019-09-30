import os, sys
from scrapy.cmdline import execute

from redis import Redis

# 获取redis连接对象
redis = Redis()

redis.lpush("ysw:start_urls", 'http://www.esw.com.cn/company/default.aspx?page=434')


# 关闭redis
redis.close()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "ysw"])
