# -*- coding: utf-8 -*-
import scrapy
import re
import urllib
from ..items import *
from scrapy_redis.spiders import RedisSpider


class LbwSpider(RedisSpider):
    name = 'lbw'
    redis_key = 'lbw:start_urls'

    def parse(self, res):
        try:
            companies = res.xpath("//div[@class='company-info']")
            for company in companies:
                # 提取公司名
                name = company.xpath("./div/a").extract_first()
                name = re.sub("<.*?>|\s", "", name) if name else ""

                url = company.xpath("./div/a/@href").extract_first()

                # 提取公司服务
                service = company.xpath("./dl[@class='co-i-program']/dd").extract_first()
                service = re.sub("<.*?>|\s", "", service) if service else ""

                # 提取公司电话
                phone = company.xpath("./dl[@class='co-i-phone']/dd/text()").extract_first()

                # 提取公司地址
                address = company.xpath("./dl[@class='co-i-address']/dd/text()").extract_first()
                item = LbwscrapyItem()
                item["name"] = name
                item["service"] = service
                item["phone"] = phone
                item["address"] = address
                item["url"] = url
                # print(item)
                yield item

            # 翻页
            next_page = res.xpath("//li[@class='next']/a/@href").extract_first()
            if len(companies) and next_page:
                yield scrapy.Request(url=next_page, callback=self.parse)
        except Exception as e:
            print(e)
            # tags = res.xpath(".//dl/dt/text()").extract()
            # tags = map(lambda x: re.sub("\s", "", x), tags) if len(tags) else []
            # n = len(tags)
            # for i in range(n):
            #     if tags[i] == "服务项目：":
            #         service = res.xpath(".//dl/dd").extract_first()
            #         service = re.sub("<.*?>|\s", "", service) if service else ""
            #
            #     elif tags[i] == "地址：":
            #         address = res.xpath(".//dl/dd/text()").extract_first()
            #
            #     elif tags[i] == "地址：":
            #         address = res.xpath(".//dl/dd/text()").extract_first()

