# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StoreItem(scrapy.Item):
    # define the fields for your item here like:
    # 店铺名
    name = scrapy.Field()
    # 店铺地址
    address = scrapy.Field()
    # 店铺电话
    phone = scrapy.Field()
    telephone = scrapy.Field()
    # 店铺商品种类
    kind = scrapy.Field()
    # 店铺省份
    province = scrapy.Field()
    # 店铺城市
    city = scrapy.Field()
    # 店铺url
    url = scrapy.Field()
