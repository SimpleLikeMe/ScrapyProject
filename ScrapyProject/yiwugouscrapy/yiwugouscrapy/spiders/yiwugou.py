# -*- coding: utf-8 -*-
import scrapy
import re
from .. import items


class YiwugouSpider(scrapy.Spider):
    name = 'yiwugou'
    allowed_domains = ['www.yiwugo.com']
    start_urls = ['https://www.yiwugo.com/']

    def __init__(self):
        super(YiwugouSpider, self).__init__()
        self.kind_count = 0
        self.url_count = 0
        self.info_count = 0

    def parse(self, response):
        print(f"提取城市分区:{response}")
        areas = response.xpath("//div[@class='index-market-bord']")
        # print(res)
        # print(len(res))
        urls1 = list()
        for area in areas:
            carea = area.xpath(".//div[@class='index-market-left']/a[@class='sctitile']/text()").extract()
            carea = carea[0] if len(carea) else ""
            # print(carea)
            urls = [{"area": carea, 'url': f'https://www.yiwugo.com/{i.xpath("./@href").extract()[0]}',
                     'kind': i.xpath("./text()").extract()[0]} for i in area.xpath(".//ul/li/span/a")]
            urls.extend([{"area": carea, 'url': f'https://www.yiwugo.com/{i.xpath("./@href").extract()[0]}',
                          'kind': i.xpath("./text()").extract()[0]} for i in area.xpath(".//ul/li/span/span/a")])
            urls1.extend(urls)
        for url in urls1:
            # item = items.AreaUrlscrapyItem()
            item = items.StoreInfoItem()
            item["area"] = url.get("area")
            item["kind"] = url.get("kind")
            # item["url"] = url.get("url")
            # self.kind_count += 1
            # print("种类item数:", self.kind_count)
            # yield item
            yield scrapy.Request(url=url.get("url"), meta={'item': item}, callback=self.parse_store_url)
            # print(url)

    def parse_store_url(self, response):
        urls = ["https://www.yiwugo.com" + i for i in response.xpath("//div[@class='search_pro_left ']//ul/li[@class='font_tit titheight']/a/@href").extract()]
        for url in urls:
            item = items.StoreUrlItem()
            item["down_url"] = url
            item["up_url"] = response.url
            # self.url_count += 1
            # print("店铺url数:", self.kind_count)
            # 保存url
            yield item
            try:
                # 请求店铺主页
                yield scrapy.Request(url=url, meta={"item": response.meta['item']}, callback=self.parse_store_info)
            except Exception as e:
                print(e)
                continue
        # 翻页
        next_page = response.xpath("//ul/a[@class='page_next_yes']/@href").extract()
        if len(next_page):
            next_page = "https://www.yiwugo.com" + next_page[0]
            yield scrapy.Request(url=next_page, callback=self.parse_store_url)

    def parse_store_info(self, response):
        # 店铺名
        name = response.xpath("//ul[@class='shop_introduce']/li[1]/span/text()").extract()
        name = re.sub(r"\W", "", name[0]) if len(name) else " "
        # 手机
        phone = response.xpath("//ul[@class='shop_introduce']/li[contains(@class,'c666 ico-shop-02')]/text()").extract()
        phone = re.sub(r"\W", "", phone[0]) if len(phone) else " "
        # 电话
        telephone = response.xpath("//ul[@class='shop_introduce']/li[contains(@class,'c666 ico-shop-03')]/text()").extract()
        telephone = re.sub(r"\W", "", telephone[0]) if len(telephone) else " "
        # phone1 = html.xpath("//ul[@class='shop_introduce']/li[@class='c666 ico-shop-03']/@text()")
        # 地址
        address = response.xpath("//ul[@class='shop_introduce']/li/span[@class='con']/text()").extract()
        n = len(address)
        for i in range(n):
            d = re.sub(r"\W", "", address[i])
            if d:
                address = d
                break
        else:
            address = ""
        # item = items.StoreInfoItem()
        item = response.meta['item']
        item["name"] = name
        item["phone"] = phone
        item["telephone"] = telephone
        item["address"] = address
        item["url"] = response.url
        item["city"] = "义乌市"
        item["province"] = "浙江省"
        # self.info_count += 1
        # print("店铺信息数：", self.info_count)
        yield item
