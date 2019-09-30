# -*- coding: utf-8 -*-
import scrapy
import base64
from fontTools.ttLib import TTFont
import re
from ..items import *


class GysSpider(scrapy.Spider):
    name = 'gys'
    # allowed_domains = ['www.china.cn/search/ewma.shtml?t=1']
    start_urls = ['https://shenzhen.china.cn/search/g8j09.shtml']

    def parse(self, res):
        lis = res.xpath("//ul[@class='extension_ul']/li")
        print(lis)
        for li in lis:
            # 获取公司名称
            name = li.xpath("./div[@class='extension_right']/p[1]/a/text()").extract_first()
            name = re.sub("<.*?>", "", name) if name else ""
            # 获取url
            url = li.xpath("./div[@class='extension_right']/p[1]/a/@href").extract_first()
            # 获取主营产品
            product = li.xpath("./div[@class='main_products']").extract_first()
            product = re.sub("<.*?>", "", product) if product else ""
            product = re.sub("\s", ";", product) if product else ""
            # 构建item对象
            item = GysscrapyItem()
            item["name"] = name
            item["product"] = product
            item["url"] = url
            item["referer"] = res.url
            req = scrapy.Request(url=url, callback=self.parse_detail, meta={"item": item})
            host = url.split("/")[-1]
            req.headers["Host"] = host
            yield req
            # break

        # 翻页
        next_page = res.xpath("//a[@class='rollPage']/@href").extract_first()
        print("next:", next_page)
        # if len(lis) and next_page:
        #     yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_detail(self, res):
        phone = self.parse_phone(res.text)
        item = res.meta["item"]
        item["phone"] = phone
        dls = res.xpath("//div[@id='contact']//ul[@class='dot2'][1]/li/dl")
        for dl in dls:
            tag_name = re.sub("\W", "", dl.xpath("./dt/text()").extract_first())
            # print(tag_name)
            if tag_name == "地址":
                address = re.sub("\s", "", dl.xpath("./dd/text()").extract_first())
                # print(f"address:{address}")
                item["address"] = address
                yield item
                break
        # print(item)

    def parse_phone(self, html):
        """获取电话号码"""
        # 0-9数字映射
        my_map = {
            '126983rmoveto-680rlineto07rlineto160rlineto503307rrcurveto00rlineto0134rlineto06-22-5-3rrcurveto00rlineto-16-8rlineto-38rlineto3922rlineto7-4rlineto0-157rlineto0-73-350rrcurveto00rlineto160rlineto0-7rlinetoendchar': '1',
            '1263984rmoveto00rlineto-28rlineto28101415-119rrcurveto00rlineto016-78-130rrcurveto00rlineto-151-14-10-13-20rrcurveto00rlineto-63rlineto11311716231rrcurveto00rlineto26-113-121-24rrcurveto00rlineto0-15-9-13-17-12rrcurveto00rlineto25-312-150-26rrcurveto00rlineto-2-39-24-20-47-2rrcurveto00rlineto-181-95-19rrcurveto00rlineto173461rrcurveto00rlineto305-37-5rrcurveto00rlineto-11102-1rrcurveto00rlineto7-56-250rrcurveto00rlineto1931014225rrcurveto00rlineto331-1711-37-8rrcurvetoendchar': '3',
            '12611177rmoveto1010rlineto0-6rlineto-53-172rlineto-210rlineto52157rlineto-560rlineto-61-3-3-1-6rrcurveto00rlineto-7-22rlineto-60rlineto051rlinetoendchar': '7',
            '12610656rmoveto60rlineto0-53rlineto-1040rlineto07rlineto4755rlineto1720821023rrcurveto00rlineto021-810-170rrcurveto00rlineto-151-13-12-12-24rrcurveto00rlineto-72rlineto9361818260rrcurveto00rlineto28-215-161-30rrcurveto00rlineto1-18-11-21-23-25rrcurveto00rlineto-39-44rlineto520rlineto11-1710322rrcurveto00rlinetoendchar': '2',
            '12663173rmoveto00rlineto-211-11-280-56rrcurveto00rlineto-1-5811-28222rrcurveto00rlineto22-11128-157rrcurveto00rlineto056-1128-21-1rrcurveto08rmoveto00rlineto33-419-305-57rrcurveto00rlineto-3-57-19-30-35-3rrcurveto00rlineto-352-1930-259rrcurveto00rlineto4571930333rrcurvetoendchar': '0',
            '12615-1rmoveto00rlineto-27rlineto43152525735rrcurveto00rlineto-11-11-12-6-130rrcurveto00rlineto-273-1518-233rrcurveto00rlineto1411721331rrcurveto00rlineto35-118-251-49rrcurveto00rlineto0-59-33-36-66-12rrcurveto7595rmoveto00rlineto253-1026-22-1rrcurveto00rlineto-190-9-160-32rrcurveto00rlineto-1-3310-16211rrcurveto00rlineto11196811rrcurvetoendchar': '9',
            '12698156rmoveto-590rlineto-8-36rlineto50125-211-42rrcurveto00rlineto-3-37-22-20-42-3rrcurveto00rlineto-200-105-19rrcurveto00rlineto083470rrcurveto00rlineto516-38-7rrcurveto00rlineto8-56-330rrcurveto00rlineto171914126rrcurveto00rlineto232-2015-42-1rrcurveto00rlineto-30-1203rrcurveto00rlineto1577rlineto740rlineto-4-16rlineto0-3-2-2-30rrcurveto00rlinetoendchar': '5',
            '126111181rmoveto00rlineto0-8rlineto-43-12-25-25-7-39rrcurveto00rlineto109115120rrcurveto00rlineto29-216-182-34rrcurveto00rlineto-3-35-18-19-33-3rrcurveto00rlineto-351-1823-145rrcurveto00rlineto56334376312rrcurveto-50-85rmoveto00rlineto-90-9-3-9-6rrcurveto00rlineto-1-120-91-7rrcurveto00rlineto1-3610-18191rrcurveto00rlineto1911015030rrcurveto00rlineto130-1115-22-1rrcurvetoendchar': '6',
            '1269460rmoveto250rlineto0-20rlineto-250rlineto0-41rlineto-200rlineto041rlineto-700rlineto019rlineto78122rlineto120rlineto0-121rlineto-790rmoveto590rlineto092rlineto-59-92rlinetoendchar': '4',
            '1265483rmoveto00rlineto-16-11-8-131-15rrcurveto00rlineto1-2311-1221-1rrcurveto00rlineto1921011119rrcurveto00rlineto015-1415-2715rrcurveto8-84rmoveto00rlineto-312-1714-325rrcurveto00rlineto-11811172315rrcurveto00rlineto-2114-1016118rrcurveto00rlineto2271514292rrcurveto00rlineto27-215-132-24rrcurveto00rlineto1-16-10-14-21-13rrcurveto00rlineto27-1513-18-1-22rrcurveto00rlineto-1-29-17-15-33-1rrcurveto-27148rmoveto00rlineto-1-1410-1421-14rrcurveto00rlineto1512813014rrcurveto00rlineto-118-1010-191rrcurveto00rlineto-15-1-8-9-1-16rrcurvetoendchar': '8',
            '14012694rmoveto0-17rlineto-1130rlineto017rlineto1130rlinetoendchar': '-'}
        try:
            # 获取base64加密的字体
            base64_string = html.split("base64,")[1].split("'")[0]
            # 使用base64库对加密字体进行解码
            bin_data = base64.decodebytes(base64_string.encode())
            # 将字体保存到本地
            with open(f"./fonts/{base64_string[:50]}.woff", r"wb") as f:
                f.write(bin_data)
            # 使用TTFont打开文件
            font = TTFont(f"./fonts/{base64_string[:50]}.woff")
            # 将文件保存为xml格式
            font.saveXML(f"./fonts/{base64_string[:50]}.xml")

            # 打开保存的xml字体关系映射表
            with open(f"./fonts/{base64_string[:50]}.xml", mode="r", encoding="utf-8") as f:
                tables = f.read()

            # 获取对应的关系映射
            lis = re.findall('<CharStringname=".*?">.*?</CharString>', re.sub("\s", "", tables))
            # 通过对象关系映射构建规则字典（将Unicode编码和对应的字体构建映射）
            rule_dict = {}
            for li in lis:
                # 获取所有的key
                key = re.findall('<CharStringname="(.*?)">', li)
                if not len(key):
                    continue
                key = re.sub("uni", "", key[0])

                # 获取所有的值
                value = re.findall('<CharStringname.*?>(.*?)<.*?>', li)
                if not len(value):
                    continue
                value = value[0]
                # 构建键值对映射
                rule_dict[key] = value

            # 获取手机号码
            phone = re.findall('<span class="secret">(.*?)</span>', html)
            phone_list = re.findall('&#x(\w+)', phone[0]) if len(phone) else ""
            phone = ""
            # 遍历每一个电话号码（形如：['1001f', '10020', '10021', '10022', '1001f', '10021', '1001f', '10023', '10024', '10025', '10021']）
            for num in phone_list:
                # 通过num获取my_map中数字对应的键
                key = rule_dict[num]
                phone += my_map.get(key)
        except Exception as e:
            print(e)
            return

        return phone
