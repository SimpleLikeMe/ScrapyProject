# -*- coding: utf-8 -*-

# Scrapy settings for huangyescrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'huangyescrapy'

SPIDER_MODULES = ['huangyescrapy.spiders']
NEWSPIDER_MODULE = 'huangyescrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Host': 'so.huangye88.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.huangye88.com/',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_c8184fd80a083199b0e82cc431ab6740=1569718926,1569733767,1569805781,1569810366; hy88loginid=3067736; hy88username=u3067736; hy88usergroup=12; hy88mobile=18438620783; UM_distinctid=16d76a885f59c4-0029f424203d628-4c312373-1fa400-16d76a885f62e8; CNZZDATA1275188542=288583334-1569652353-http%253A%252F%252Fwww.huangye88.com%252F%7C1569652353; hy88showeditems=a%3A2%3A%7Bi%3A111505685%3Ba%3A2%3A%7Bs%3A7%3A%22subject%22%3Bs%3A75%3A%22%E6%96%B0%E4%B9%A1%E7%94%B5%E5%8A%A8%E8%80%81%E7%88%B7%E8%BD%A6%E6%96%B0%E4%B9%A1%E7%94%B5%E5%8A%A8%E8%80%81%E7%88%B7%E8%BD%A6%E4%BB%B7%E6%A0%BC%E6%96%B0%E4%B9%A1%E7%94%B5%E5%8A%A8%E8%80%81%E7%88%B7%E8%BD%A6%E5%8E%82%E5%AE%B6%22%3Bs%3A3%3A%22url%22%3Bs%3A56%3A%22http%3A%2F%2Fzhengzhou.huangye88.com%2Fxinxi%2F3523_111505685.html%22%3B%7Di%3A111535698%3Ba%3A2%3A%7Bs%3A7%3A%22subject%22%3Bs%3A75%3A%22%E6%B2%B3%E5%8D%97%E7%94%B5%E5%8A%A8%E8%80%81%E7%88%B7%E8%BD%A6%E6%B2%B3%E5%8D%97%E7%94%B5%E5%8A%A8%E8%80%81%E7%88%B7%E8%BD%A6%E4%BB%B7%E6%A0%BC%E6%B2%B3%E5%8D%97%E7%94%B5%E5%8A%A8%E8%80%81%E7%88%B7%E8%BD%A6%E5%8E%82%E5%AE%B6%22%3Bs%3A3%3A%22url%22%3Bs%3A56%3A%22http%3A%2F%2Fzhengzhou.huangye88.com%2Fxinxi%2F3523_111535698.html%22%3B%7D%7D; gr_user_id=0e5e7d46-578d-4626-b059-df279c3b32c9; Hm_lpvt_c8184fd80a083199b0e82cc431ab6740=1569813194; PHPSESSID=15697189950576-1693c90d1d91e93d410bb106e1ba5ef3f73f7aa0; BAIDU_SSP_lcr=https://www.baidu.com/link?url=IjnrCZfsrf1phxSOTojhxpiJQfg8Dhi8YzvR2A2XS0vZ75NjB1UOxYMp01TVuFiJ&wd=&eqid=b28b33630026a838000000035d903c7d',
    'Upgrade-Insecure-Requests': '1', 'Cache-Control': 'max-age=0'
}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'huangyescrapy.middlewares.HuangyescrapySpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'huangyescrapy.middlewares.HuangyescrapyDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'huangyescrapy.pipelines.HuangyescrapyPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 配置redis数据库
REDIS_URL = 'redis://root:jiefutong@114.116.126.177:6379'

# 调度器组件设置(将调度器替换为scrapy-redis)
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 持久化存储
SCHEDULER_PERSIST = True
# redis编码
REDIS_ENCODING = "utf-8"
# 日志等级
LOG_LEVEL = 'DEBUG'
# 每次爬取都清空
SCHEDULER_FLUSH_START = False
# 配置重爬，爬虫异常中断重新启动爬虫会继续接着上次的爬取（单机爬虫使用）
SCHEDULER_FLUSH_ON_START = True

# 配置mysql数据库
MYSQL_TABLE = "hy_store"
MYSQL_USER = "meituan_cate"
MYSQL_PASSWORD = "54dsWWPnGMyhdKzH"
MYSQL_HOST = "114.116.126.177"
MYSQL_PORT = 6653
MYSQL_DB = "meituan_cate"
