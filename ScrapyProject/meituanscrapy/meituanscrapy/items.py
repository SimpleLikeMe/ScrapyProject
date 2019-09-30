# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PageUrlItem(scrapy.Item):
    url = scrapy.Field()
    page = scrapy.Field()


class IdsItem(scrapy.Item):
    sid = scrapy.Field()
    url = scrapy.Field()


class StoreInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # 店铺名
    name = scrapy.Field()
    # 电话
    phone = scrapy.Field()
    # 店铺地址
    address = scrapy.Field()
    url = scrapy.Field()
    # # 店铺区域
    # area = scrapy.Field()
    # # 美食分类
    # cate = scrapy.Field()
