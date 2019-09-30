import os, sys
from scrapy.cmdline import execute

from redis import Redis

# 获取redis连接对象
# redis = Redis(host="114.116.126.177", password="jiefutong", db=0)
# # redis = Redis()
# redis.lpush("lbw:start_urls", 'http://b2b.liebiao.com/sou-gs/毛巾/?pn=1')


# 关闭redis
# redis.close()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "lbw"])
