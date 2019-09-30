# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StoreUrlItem(scrapy.Item):
    # define the fields for your item here like:
    down_url = scrapy.Field()
    up_url = scrapy.Field()


class AreaUrlscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    area = scrapy.Field()
    kind = scrapy.Field()
    url = scrapy.Field()


class StoreInfoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    telephone = scrapy.Field()
    url = scrapy.Field()
    kind = scrapy.Field()
    area = scrapy.Field()
    city = scrapy.Field()
    province = scrapy.Field()
