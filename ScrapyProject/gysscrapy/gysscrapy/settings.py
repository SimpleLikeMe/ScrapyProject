# -*- coding: utf-8 -*-

# Scrapy settings for gysscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'gysscrapy'

SPIDER_MODULES = ['gysscrapy.spiders']
NEWSPIDER_MODULE = 'gysscrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Host': 'www.china.cn',
    'Referer': 'https://cn.china.cn/',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1', 'TE': 'Trailers',
    'Cookie': 'Hm_lvt_066cf190c4bdf8653ad5ea8f496c4a13=1568773187,1568773313,1568774536,1568779647; Hm_lvt_60030dce41abe35fdcca4338a88126a7=1568710610,1568779397,1568787516,1568793378; china_uv=718fc9b75bcbe8e9ddfe06ed1c702fa5; Hm_lvt_6633f2c221756b56fb625ded6d946372=1568687092; SMTKF_visitor_id_39034=212647152; BAIDU_SSP_lcr=https://www.baidu.com/link?url=8G7P1-9LCKbqeytFDS73KnIIWqt8mupcoZgOUtnk7jm&wd=&eqid=8d59b3fc001c0990000000035d818d17; Hm_lpvt_066cf190c4bdf8653ad5ea8f496c4a13=1568787926; PHPSESSID=26fb9e522b433ff6a7b6bf0ee3fc4b03; Hm_lpvt_60030dce41abe35fdcca4338a88126a7=1568793378; U=id%3D4470149566%26k%3D06719493%26cid%3D4470149562%26cid_k%3D225a2a12%26n%3Dsimplelikeme%26usertype%3D1%26contact%3Dsimple%26super%3D0%26l%3D1%26expire%3D1569398160; Hm_lvt_eacc334f8eb162234e4fc886d62315dc=1568788914; Hm_lpvt_eacc334f8eb162234e4fc886d62315dc=1568788914; CS=c%3D4470149562%26l%3D0%26t%3D1',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'gysscrapy.middlewares.GysscrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'gysscrapy.middlewares.GysscrapyDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'gysscrapy.pipelines.GysscrapyPipeline': 300,
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
