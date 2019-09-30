# -*- coding: utf-8 -*-

# Scrapy settings for alibabascrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'alibabascrapy'

SPIDER_MODULES = ['alibabascrapy.spiders']
NEWSPIDER_MODULE = 'alibabascrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 3
CONCURRENT_REQUESTS_PER_IP = 3

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
HEADERS = {'Host': 's.1688.com',
           # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive',
           # 'Referer': 'https://s.1688.com/company/company_search.htm?keywords=%C8%B9%D7%B0&sortType=pop&n=y&filt=y',
           'Cookie': '_lastvisited=%2FwkAFiTzQHoCAd9YN7AIJ%2FGm%2C%2CwkAFiTzQHoCAd9YN7AIJGm4ptIEGdhlX%2Ck0km9gvj%2Ck0km9gvj%2C3%2C7f71aae3%2C%2FwkAFiTzQHoCAd9YN7AIJ%2FGm%2Ck0km9gvk; _uab_collina=156821811749549725433317; _umdata=GCA659EDC861AEDE92C131ABA2E240CEB7E5836',
           'Upgrade-Insecure-Requests': '1', 'TE': 'Trailers'}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'alibabascrapy.middlewares.AlibabascrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'alibabascrapy.middlewares.AlibabascrapyDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'alibabascrapy.pipelines.AlibabascrapyPipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline': 300,
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


# redis配置
REDIS_HOST = "114.116.126.177"  # 主机名
REDIS_PORT = 6379  # 端口号
REDIS_PARAMS = {
    'password': 'jiefutong',
}

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

# 代理地址
# PROXY_URL = "http://127.0.0.1:5555/random"


# 配置mysql数据库
MYSQL_TABLE = "ali_store"
MYSQL_USER = "meituan_cate"
MYSQL_PASSWORD = "54dsWWPnGMyhdKzH"
MYSQL_HOST = "114.116.126.177"
MYSQL_PORT = 6653
MYSQL_DB = "meituan_cate"
