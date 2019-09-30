# -*- coding: utf-8 -*-
import scrapy
import re
import urllib
from ..items import *
from scrapy_redis.spiders import RedisSpider


class YswSpider(RedisSpider):
    name = 'ysw'
    # allowed_domains = ['www.esw.com.cn/company']
    # start_urls = ['http://www.esw.com.cn/company/']
    # start_urls = ['http://www.esw.com.cn/company/', 'http://www.esw.com.cn/company/default.aspx?page=4337', 'http://www.esw.com.cn/company/default.aspx?page=4336']
    redis_key = 'ysw:start_urls'

    def parse(self, res):
        company = res.xpath("//div[@class='yllist']/ul/li/div[1]")
        for cpn in company:
            # name = re.sub("\s", "", cpn.xpath("./p/span[@class='f14t']/a/text()").extract_first())

            all_info = cpn.xpath("./p").extract_first().split("<br>")
            # all_info = re.sub("<.*?>", "", cpn.xpath("./p").extract_first())
            # all_info = list(map(lambda x: re.sub("\s", "", x), all_info.split("\n")))
            all_info = list(map(lambda x: re.sub("<.*?>|\s", "", x), all_info))
            name = all_info[0] if len(all_info) else ""
            product = re.sub("主营：", "", all_info[1]) if len(all_info) >= 1 else ""
            address = re.findall("(.*?)邮编", all_info[2]) if len(all_info) >= 2 else ""
            address = address[0] if len(address) else ""
            # print(all_info)
            phone_contacts = re.findall("(\d{11}|\d{3,4}-\d{3,4}-\d+|\d{3,4}-\d+)(\w*)", all_info[3]) if len(all_info) >= 3 else ""
            phone_contacts = phone_contacts[0] if len(phone_contacts) else []
            phone = phone_contacts[0] if len(phone_contacts) else ""
            contacts = phone_contacts[1] if len(phone_contacts) >= 1 else ""
            # url = re.findall("公司网址：(.*?www|.*?)", all_info[4]) if len(all_info) >= 4 else ""
            url = "http://www.esw.com.cn"+re.sub("\s", "", cpn.xpath("./p/span[@class='f14t']/a/@href").extract_first())
            # print(all_info)
            # print(name, product, address, phone, contacts, url)
            item = YswscrapyItem()
            item["name"] = name
            item["product"] = product
            item["address"] = address
            item["phone"] = phone
            item["contacts"] = contacts
            item["url"] = url
            if item["phone"] and item["name"]:
                # yield item
                yield scrapy.Request(url=url, callback=self.parse_detail, meta={"item": item})

        # 翻页
        next_page = res.xpath("//div[@id='AspNetPager1']/div[2]/a[last()-1]/@href").extract_first()
        if next_page:
            yield scrapy.Request(url=res.urljoin(next_page), callback=self.parse)

    def parse_detail(self, res):
        item = res.meta["item"]
        product = re.sub("\s", "", "，".join(res.xpath("//div[@class='list_con']/h3/a/text()").extract()), re.M)
        product = item["product"] if not product else item["product"] + '，' + product
        product = re.sub("\s", "", product)
        # print(product)
        about_us = res.xpath("//div[@class='content']//dd/p").extract_first()
        # about_us = list(about_us)[0] if len(list(about_us)) else ""
        # print(about_us)
        about_us = about_us if about_us else res.xpath("//div[@class='ab-l']/div/div/span/text()").extract_first()
        about_us = about_us if about_us else res.xpath("//div[@class='ab-l']//dd//p/text()").extract_first()
        # print(about_us)
        about_us = re.sub("<.*?>|\s", "", about_us) if about_us else ""
        # print(about_us)
        #
        introduction = res.xpath("//div[@class='ab-l']/dl/dd/p").extract_first()
        introduction = re.sub("<.*?>|\s", "", introduction) if introduction else ""
        related_enterprises = ",".join(res.xpath("//ul[@id='qstList']/li/a[2]/text()").extract())
        # print(related_enterprises)
        related_enterprises = re.sub("<.*?>|\s", "", related_enterprises) if related_enterprises else ""
        # print(related_enterprises)
        item["product"] = product
        item["about_us"] = about_us
        item["introduction"] = introduction
        item["related_enterprises"] = related_enterprises
        yield item
        # print(item)
