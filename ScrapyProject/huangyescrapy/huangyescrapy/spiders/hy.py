# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import *
from scrapy_redis.spiders import RedisSpider



class HySpider(RedisSpider):
    name = 'hy'
    # allowed_domains = ['so.huangye88.com/?kw=%E4%BA%92%E8%81%94%E7%BD%91']
    # start_urls = ['http://so.huangye88.com/?kw=%E4%BA%92%E8%81%94%E7%BD%91&type=company&page=6/']
    redis_key = 'hy:start_urls'

    def parse(self, res):
        companies = res.xpath("//div[@class='conttext']")
        for company in companies:
            # 获取公司名
            name = company.xpath("./p/a/text()").extract_first()
            name = name if name else ""
            # 获取公司地址
            url = company.xpath("./p/a/@href").extract_first()
            url = url if url else ""
            # 获取联系人
            contacts = company.xpath("./ul/li[@class='fen']/text()").extract_first()
            contacts = contacts if contacts else ""

            # 获取所有的标签
            tags = company.xpath("./ul/li")
            n = len(tags)
            product = ""
            phone = ""
            address = ""
            # 提取标签中的内容
            for i in range(n):
                tag = tags[i].xpath("./label/text()").extract()

                if len(tag) and re.sub("\W", "", tag[0]) == "主营产品":
                    product = tags[i].xpath("./text()").extract_first()

                if len(tag) and re.sub("\W", "", tag[0]) == "电话号码":
                    phone = tags[i].xpath("./text()").extract_first()

                if len(tag) and re.sub("\W", "", tag[0]) == "所在地":
                    address = tags[i].xpath("./text()").extract_first()

            # 构建item
            item = HuangyescrapyItem()
            item["name"] = name
            item["contacts"] = contacts
            item["phone"] = self.filter_phone(phone)
            item["product"] = product
            item["address"] = address
            item["url"] = url
            yield item

        # 翻页
        next_page = res.xpath("//a[contains(@class,'nextpage')]/@href").extract_first()
        if len(companies) and next_page:
            yield scrapy.Request(res.urljoin(next_page), callback=self.parse)

    def filter_phone(self, phone_str):
        import re
        phone_str = "".join(re.findall("\d+", phone_str))
        phone = re.findall("1\d{10}", phone_str)
        telephone = re.findall(".*?(0\d{8,12})", phone_str)
        if len(phone):
            return phone[0]
        elif len(telephone):
            return telephone[0]
        else:
            return ""

