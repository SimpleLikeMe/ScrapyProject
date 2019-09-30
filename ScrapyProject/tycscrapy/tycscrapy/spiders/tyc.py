# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import *
from scrapy_redis.spiders import RedisSpider


class TycSpider(RedisSpider):
    name = 'tyc'
    # allowed_domains = ['www.tianyancha.com/search']
    # start_urls = ['http://www.tianyancha.com/search/p1?key=%E6%8D%B7%E4%BB%98%E9%80%9A']
    redis_key = 'tyc:start_urls'

    def parse(self, res):
        # print(res.text)
        ls = list()
        companies = res.xpath("//div[@class='search-result-single   ']")
        for company in companies:
            # 公司名
            name = company.xpath("./div[@class='content']/div[@class='header']/a").extract_first()
            name = re.sub("<.*?>|\s", "", name)
            # 详细信息网址
            url = company.xpath("./div[@class='content']/div[@class='header']/a/@href").extract()
            url = url[0] if len(url) else ""
            # 法人代表
            legal_person = company.xpath(".//a[contains(@class,'legalPersonName')]/text()").extract_first()
            # 注册资金
            capital = company.xpath(".//div[contains(@class,'-narrow')]/span/text()").extract_first()
            # 注册日期
            register_date = company.xpath(".//div[contains(@class,'text-ellipsis')]/div[3]/span/text()").extract_first()
            # 省
            province = company.xpath(".//span[@class='site']/text()").extract_first()
            # 评分
            score = company.xpath(".//span[@class='score-num']/text()").extract_first()

            # 筛选标签
            tags = company.xpath(".//div[@class='col']/span[@class='label']")
            n = len(tags)
            phone = ""
            email = ""
            his_name = ""
            business_scope = ""
            address = ""
            for i in range(n):
                tag = re.sub('\W', '', tags[i].xpath("./text()").extract_first())

                if tag == '电话':
                    phone = tags[i].xpath(".//following-sibling::span/span[1]/text()").extract_first()
                    phone = self.filter_phone(phone)
                if tag == '邮箱':
                    email = tags[i].xpath(".//following-sibling::span[1]/text()").extract_first()

            tags = company.xpath(".//i[contains(@class,'tic-match')]/following-sibling::span[@class='label']")
            n = len(tags)
            for i in range(n):
                tag = re.sub('\W', '', tags[i].xpath("./text()").extract_first())
                if tag == '历史名称':
                    his_name = tags[i].xpath(".//following-sibling::span[1]/text()").extract_first()

                if tag == '经营范围':
                    business_scope = tags[i].xpath(".//following-sibling::span[1]/text()").extract_first()

                if tag == '地址信息':
                    address = tags[i].xpath(".//following-sibling::span[1]/text()").extract_first()

            # if phone:
            item = TycscrapyItem()
            item["name"] = name
            item["phone"] = phone
            item["email"] = email
            item["score"] = score
            item["capital"] = capital
            item["register_date"] = register_date
            item["legal_person"] = legal_person
            item["province"] = province
            item["url"] = url
            item["his_name"] = his_name
            item["business_scope"] = business_scope
            item["address"] = address
            yield item
                # ls.append({"name": name, "phone": phone, "email": email, "score": score, "capttal": capital,
                #            "regist_date": register_date, "legal_person": legal_person, "province": province})
            # print({"name": name, "phone": phone, "email": email, "score": score, "capttal": capital,
            #        "regist_date": register_date, "legal_person": legal_person, "province": province, "url": url})

        # 翻页
        if len(companies):
            next_page = res.xpath("//li/a[contains(@class, '-next')]/@href").extract_first()
            print(next_page)
            if next_page:
                yield scrapy.Request(url=next_page, callback=self.parse)

    def filter_phone(self, phone_str):
        import re
        try:
            phone_str = "".join(re.findall("\d+", phone_str))
            phone = re.findall("1\d{10}", phone_str)
            telephone = re.findall(".*?(0\d{8,12})", phone_str)
            if len(phone):
                return phone[0]
            elif len(telephone):
                return telephone[0]
            else:
                return ""
        except Exception as e:
            print(e)
            return ""
