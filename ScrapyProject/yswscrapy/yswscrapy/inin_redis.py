from redis import Redis

# 获取redis连接对象
redis = Redis()

redis.lpush("ysw:start_urls", 'http://www.esw.com.cn/company/')


# 关闭redis
redis.close()
