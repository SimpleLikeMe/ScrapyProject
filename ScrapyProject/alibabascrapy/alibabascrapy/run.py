import os, sys
from scrapy.cmdline import execute

from redis import Redis

# 获取redis连接对象
redis = Redis(host='114.116.126.177', password='jiefutong')
# redis = Redis()
redis.lpush("alibaba:start_urls", 'https://s.1688.com/company/company_search.htm?keywords=%BC%C7%D0%D4&city=%C9%EE%DB%DA&province=%B9%E3%B6%AB&n=y&filt=y')

# 关闭redis
redis.close()


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "alibaba"])
