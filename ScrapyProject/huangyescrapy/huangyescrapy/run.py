import os, sys
from scrapy.cmdline import execute

from redis import Redis

# # 获取redis连接对象
# redis = Redis(host='114.116.126.177', password='jiefutong')
# # redis = Redis()
# redis.lpush("hy:start_urls", 'http://so.huangye88.com/?kw=服装&type=company&')
#
# # 关闭redis
# redis.close()


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "hy"])
