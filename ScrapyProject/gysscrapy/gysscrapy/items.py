# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GysscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    product = scrapy.Field()
    address = scrapy.Field()
    url = scrapy.Field()
    phone = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    kind = scrapy.Field()
    referer = scrapy.Field()


