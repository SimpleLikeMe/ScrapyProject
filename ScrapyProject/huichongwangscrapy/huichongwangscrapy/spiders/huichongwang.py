import re
from scrapy.http import Request
from urllib import parse

from scrapy_redis.spiders import RedisSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from ..items import *


class HuiChongWangSpider(RedisSpider):
    name = 'huichongwang'
    # allowd_domains = ["//"]
    redis_key = 'huichongwang:start_urls'
    # rules = (
    #     # follow all links
    #     Rule(LinkExtractor(), callback='parse_detail', follow=True),
    # )
    #
    # def parse_page(self, response):
    #     return {
    #         'name': response.css('title::text').extract_first(),
    #         'url': response.url,
    #     }

    def parse(self, response):

        """
        逻辑分析
            1.通过抓取下一页的链接，交给scrapy实现自动翻页,如果没有下一页则爬取完成
            2.将本页面的所有文章url爬下，并交给scrapy进行深入详情页的爬取
        """
        # print(response)
        hrefs = response.xpath("//div[@class='moreproduct']/a[2]/@href")
        # print(len(hrefs), hrefs)
        city = parse.unquote(response.url.split("?")[1].split("&")[2].split(":")[-1])
        province = parse.unquote(response.url.split("?")[1].split("&")[2].split(":")[-2])
        kind = parse.unquote(response.url.split("?")[1].split("&")[0].split("=")[1])
        # print(province, city, kind)
        for href in hrefs:
            url = "https:" + href.extract()
            item = StoreItem()
            item["kind"] = kind
            item["city"] = city
            item["province"] = province
            # print(url)
            res = Request(url=url, callback=self.parse_detail, meta={"item": item}, dont_filter=True)
            host = url.split("/")[2]
            # print("host:", host)
            res.headers["Host"] = host
            z = f"{'中国'}:{province}:{city}"
            param = parse.urlencode({"kw": kind, "k": "0", "z": z})
            referer = f'{"https://s.hc360.com/company/search.html"}?{param}'
            # print(referer)
            res.headers["Referer"] = referer
            yield res
        print(len(hrefs))

        # 翻页
        next_page = response.xpath("//span[@class='page_next page-n']/a/@href").extract()
        next_page = f"https:{next_page[0]}" if len(next_page) else ""
        print("下一页：", next_page)
        if next_page:
            yield Request(next_page, callback=self.parse, dont_filter=True)
            # yield Request(url=parse.urljoin(response.url, next_page), callback=self.parse)
            # res = Request(parse.urljoin(response.url, next_page), callback=self.parse_detail, dont_filter=True)
            # res.headers["Referer"] = response.url
            # yield res

    def parse_detail(self, response):
        """
        将爬虫爬取的数据送到item中进行序列化
        这里通过ItemLoader加载item
        """
        print("详情页面：", response)
        # print("商家信息界面：", response)
        item = response.meta.get("item")
        phone1 = response.xpath("//div[@class='com-xx']/a[1]/@onclick").extract()
        address = response.xpath("//div[@class='company-words']/div[5]/em/text()")
        address = re.sub("\s|：", "", address[0].extract()) if len(address) else ""
        name = response.xpath("//div[@class='com-xx-box'][1]/div[1]/a/text()")
        name = re.sub("\s", "", name[0].extract()) if len(name) else ""
        item["url"] = response.url
        # print("item:", item)
        # print("phone1:", phone1)
        if len(phone1):
            phone1 = re.findall(r"changeSpanValue\((.*?)\);", phone1[0])
            phone1 = re.sub("'", "", phone1[0]) if len(phone1) else ""
            t_p = phone1.split(",")
            # print("phone11", phone1)
            if len(t_p) >= 2:
                telephone1 = t_p[0]
                phone1 = t_p[1]
                item["name"] = name
                item["telephone"] = telephone1
                item["phone"] = phone1
                item["address"] = address
                # print("item1:", item)

        if item.get("name") and (item.get("telephone") or item.get("phone")):
            # print("all_item:", item)
            yield item
        else:
            url = response.xpath("//div[@class='ContacCon3']/ul")
            if len(url):
                name = url[0].xpath("./li[1]/div/text()")
                name = name[0].extract() if len(name) else ""
                # print("name:", name)
                address = url[0].xpath(
                    "./li/div[@class='con3Left']/em[@class='addressIco']/parent::*/following-sibling::div/text()")
                address = re.sub("\s", "", address[0].extract()) if len(address) else ""
                phone = url[0].xpath(
                    "./li/div[@class='con3Left']/em[@class='mobileIco']/parent::*/following-sibling::div/text()")
                phone = phone[0].extract() if len(phone) else ""
                telephone = url[0].xpath(
                    "./div[@class='con3Left']/em[@class='telephoneIco']/parent::*/following-sibling::div/text()")
                telephone = re.sub("\s", "", telephone[0].extract()) if len(telephone) else ""
                # print("phone:", phone)
                # print("telephone:", telephone)
                # print("address:", address)
                if name and (telephone or phone):
                    item["name"] = name
                    item["telephone"] = telephone
                    item["phone"] = phone
                    item["address"] = address
                    # print("all_item1:", item)
                    yield item
