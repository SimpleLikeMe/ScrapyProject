# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TycscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    score = scrapy.Field()
    capital = scrapy.Field()
    register_date = scrapy.Field()
    legal_person = scrapy.Field()
    province = scrapy.Field()
    url = scrapy.Field()
    his_name = scrapy.Field()
    business_scope = scrapy.Field()
    address = scrapy.Field()


