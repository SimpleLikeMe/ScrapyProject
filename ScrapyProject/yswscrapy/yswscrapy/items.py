# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YswscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    product = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    contacts = scrapy.Field()
    url = scrapy.Field()
    about_us = scrapy.Field()
    introduction = scrapy.Field()
    related_enterprises = scrapy.Field()
