# -*- coding: utf-8 -*-

# Scrapy settings for tycscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tycscrapy'

SPIDER_MODULES = ['tycscrapy.spiders']
NEWSPIDER_MODULE = 'tycscrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Host': 'www.tianyancha.com',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive',
    'Referer': 'https://www.tianyancha.com/search?key=%E6%8D%B7%E4%BB%98%E9%80%9A',
    'Cookie': 'aliyungf_tc=AQAAADe8U2yByQ4AQAYLqymBxnJ7HzPU; csrfToken=SIg17Y_D51PoQaj0jXXnuXUp; TYCID=331b45b0deab11e9bb4b3fbf54f3eb27; undefined=331b45b0deab11e9bb4b3fbf54f3eb27; ssuid=3858421013; bannerFlag=undefined; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1569316251; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1569316494; _ga=GA1.2.844000090.1569316251; _gid=GA1.2.1392147104.1569316251; token=99e2a17e1e864813ad89fba84b2f3312; _utm=79603423dd1945c5a8f3acdf3643981f; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25227%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522surday%2522%253A%25221060%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25229%2522%252C%2522onum%2522%253A%25221%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM2MTk1Nzc3NyIsImlhdCI6MTU2OTMxNjQ5MiwiZXhwIjoxNjAwODUyNDkyfQ.wn6scAHSZp8l2iMDJPNg3pBbRm4P_1xnwruUbvVjh6IIYQiCzcpnE-GZsogSnMV_B0BWgnjXbM2HHGLiDSgi1w%2522%252C%2522vipToTime%2522%253A%25221660879563333%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E4%25BF%259D%25E7%25BD%2597%25C2%25B7%25E6%25B2%2583%25E5%2585%258B%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522isExpired%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25221%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%252250%2522%252C%2522mobile%2522%253A%252213361957777%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM2MTk1Nzc3NyIsImlhdCI6MTU2OTMxNjQ5MiwiZXhwIjoxNjAwODUyNDkyfQ.wn6scAHSZp8l2iMDJPNg3pBbRm4P_1xnwruUbvVjh6IIYQiCzcpnE-GZsogSnMV_B0BWgnjXbM2HHGLiDSgi1w',
    # 'Cookie': 'jsid=SEM-BAIDU-PZ1907-SY-000100; TYCID=29b962e0deab11e998771744057ce031; undefined=29b962e0deab11e998771744057ce031; ssuid=3803846929; _ga=GA1.2.718529824.1569316235; aliyungf_tc=AQAAAKyGwTODmwcAaHwPq1z+DuZ2eVP4; csrfToken=kpWjdaNtWxlDhXJUAbRqe6bD; bannerFlag=undefined; RTYCID=5aeafbd69d0c4ca29a449154fbd8e902; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1569316235,1569495811; _gid=GA1.2.362474333.1569495812; CT_TYCID=6f8dec53f9694b2c901d84a7047bd541; cloud_token=9fa45c622c404636b8aa14d427dd91ec; cloud_utm=4e996be6dc464bf79f15b5796ba6fbcc; token=22d29dad772448e1a1b4e87a48e232c1; _utm=1eed28f4e6fa47dcb4e256f3331fa27d; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E6%259D%258E%25E7%25BB%2585%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODQzODYyMDc4MyIsImlhdCI6MTU2OTQ5NjI2OSwiZXhwIjoxNjAxMDMyMjY5fQ.kqMvHw-9EW9dmpR7yrCQRMyF8gTtS-eThac7HXbitriz7Y4Yds06vecQl8dov9vl8NYJZtm_gASWYG1N9ApVng%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218438620783%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODQzODYyMDc4MyIsImlhdCI6MTU2OTQ5NjI2OSwiZXhwIjoxNjAxMDMyMjY5fQ.kqMvHw-9EW9dmpR7yrCQRMyF8gTtS-eThac7HXbitriz7Y4Yds06vecQl8dov9vl8NYJZtm_gASWYG1N9ApVng; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1569496276',
    'Upgrade-Insecure-Requests': '1'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'tycscrapy.middlewares.TycscrapySpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'tycscrapy.middlewares.TycscrapyDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tycscrapy.pipelines.TycscrapyPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

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
MYSQL_TABLE = "tyc_store"
MYSQL_USER = "meituan_cate"
MYSQL_PASSWORD = "54dsWWPnGMyhdKzH"
MYSQL_HOST = "114.116.126.177"
MYSQL_PORT = 6653
MYSQL_DB = "meituan_cate"

# 配置代理
PROXY_URL = 'http://127.0.0.1:5555/random'
