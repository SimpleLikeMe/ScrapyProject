# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_redis.spiders import RedisSpider
from ..items import *
from urllib import parse

count = 0
class AlibabaSpider(RedisSpider):
    name = 'alibaba'
    # allowed_domains = ['s.1688.com/company']
    # start_urls = ['https://s.1688.com/company/company_search.htm?keywords=%C8%B9%D7%B0&sortType=pop&province=%B9%E3%B6%AB&n=y&pageSize=30&city=%B9%E3%D6%DD&filt=y&offset=3&beginPage=94']
    redis_key = 'alibaba:start_urls'

    def parse(self, res):
        # print(res)
        # 解析省、市、种类
        p_c_k = res.url.split("?")
        p_c_k = p_c_k[1].split("&") if len(p_c_k) >= 2 else list()
        p_c_k = {i.split("=")[0]: i.split("=")[1] for i in p_c_k}
        # 解析省
        province = p_c_k.get("province") if p_c_k.get("province") else ""
        province = parse.unquote(province, encoding="gbk")
        # print(province)
        province = province if province else res.request.meta["province"]
        # 解析城市
        city = p_c_k.get("city") if p_c_k.get("city") else ""
        city = parse.unquote(city, encoding="gbk")
        city = city if city else res.request.meta["city"]
        # 解析种类
        second_kind = p_c_k.get("keywords") if p_c_k.get("keywords") else ""
        second_kind = parse.unquote(second_kind, encoding="gbk")
        second_kind = second_kind if second_kind else res.request.meta["second_kind"]
        # 解析关联界面
        page = p_c_k.get("beginPage") if p_c_k.get("beginPage") else "1"
        # 获取所有的公司
        divs = res.xpath("//div[@id='sw_mod_searchlist']/ul/li/div[1]//div[@class='wrap']")
        for div in divs:
            # 解析url
            url = div.xpath("./div[1]/a/@href").extract()
            url = url[0] if len(url) else ''
            if not url:
                continue

            # 解析店铺名
            name = div.xpath("./div[1]/a/text()").extract()
            name = re.sub('\s', '', name[0]) if len(name) else ""
            if not name:
                continue

            # 解析主营产品
            product = ''.join(div.xpath(".//div[3]/div[1]/div[1]/a/span/text()").extract())
            # 解析公司地址
            address = div.xpath("./div[3]/div[1]/div[2]/a/@title").extract()
            address = re.sub('\s', '', address[0]) if len(address) else ''
            # 解析公司员工数
            staff = div.xpath("./div[3]/div[1]/div[3]/a/text()").extract()
            staff = re.sub('\s', '', staff[0]) if len(staff) else ''

            # 构造item
            item = AlibabascrapyItem()
            item["name"] = name
            # item["url"] = url
            item["product"] = product
            item["address"] = address
            item["staff"] = staff
            item["province"] = province
            item["city"] = city
            item["second_kind"] = second_kind
            item["page"] = page
            # yield item
            headers = res.request.headers
            host = url.split('/')[2]
            # headers["Referer"] = f"https://s.1688.com/company/company_search.htm?{params}"
            # headers["Referer"] = f"https://s.1688.com/company/company_search.htm?{params}"
            # print("headers", headers)
            req = scrapy.Request(url=url, callback=self.parse_detail, meta={"item": item})
            req.headers["Referer"] = res.url
            req.headers["Host"] = host
            yield req

        # 翻页
        # li = res.xpath("//ul[@class='sm-company-list fd-clr']/li")
        # next_page = res.xpath("//a[@class='page-next']/@href").extract_first()
        # if len(li) and next_page:
        #     yield scrapy.Request(url=next_page, callback=self.parse, meta={"second_kind": second_kind, "province": province, "city": city})

    def parse_detail(self, res):
        # print(res)
        # print(res.request.headers)
        # 获取电话
        phone = res.xpath("//dl[@class='m-mobilephone']/@data-no").extract_first()
        # print(phone)
        # print(type(phone))
        if not phone:
            # 获取电话
            phone = res.xpath("//dl[@class='m-mobilephone']/dd/text()").extract()
            phone = re.sub("\s", "", phone[0]) if len(phone) else ""
        # 获取item对象
        item = res.request.meta["item"]
        # 保存电话
        item["phone"] = phone
        # print("phone:", phone)
        # print(item)
        yield item



"""

lpush alibaba:start_urls "https://s.1688.com/company/company_search.htm?keywords=%C8%B9%D7%B0&city=%B3%B1%D6%DD&sortType=pop&province=%B9%E3%B6%AB&n=y&filt=y"
lpush alibaba:start_urls "https://s.1688.com/company/company_search.htm?keywords=%C8%B9%D7%B0&city=%B9%E3%D6%DD&sortType=pop&province=%B9%E3%B6%AB&n=y&filt=y"
lpush alibaba:start_urls "https://s.1688.com/company/company_search.htm?keywords=%C5%AE%D7%B0&city=%C3%B7%D6%DD&sortType=pop&province=%B9%E3%B6%AB&n=y&filt=y"

"""