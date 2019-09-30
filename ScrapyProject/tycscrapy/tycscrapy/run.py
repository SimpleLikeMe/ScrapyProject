import os, sys
from scrapy.cmdline import execute

from redis import Redis

# 获取redis连接对象
redis = Redis(host="114.116.126.177", password="jiefutong", db=0)
# redis = Redis()
redis.lpush("tyc:start_urls", 'http://www.tianyancha.com/search/p1?key=%E6%8D%B7%E4%BB%98%E9%80%9A')

# 关闭redis
redis.close()


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "tyc"])
