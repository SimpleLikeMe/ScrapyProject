# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AlibabascrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    phone = scrapy.Field()
    product = scrapy.Field()
    address = scrapy.Field()
    staff = scrapy.Field()
    first_kind = scrapy.Field()
    second_kind = scrapy.Field()
    city = scrapy.Field()
    province = scrapy.Field()
    url = scrapy.Field()
    page = scrapy.Field()
