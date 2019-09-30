from redis import Redis


# 获取redis连接对象
redis = Redis(host='114.116.126.177', password='jiefutong')
# redis = Redis()
redis.lpush("hy:start_urls", 'http://so.huangye88.com/?kw=%E4%BA%92%E8%81%94%E7%BD%91&type=company&')

# 关闭redis
redis.close()
