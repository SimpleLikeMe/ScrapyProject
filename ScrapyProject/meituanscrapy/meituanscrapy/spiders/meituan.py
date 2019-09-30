# -*- coding: utf-8 -*-
import scrapy
import time
import base64
import zlib
import re
import json
from scrapy import Request
from .. import items


class MeituanSpider(scrapy.Spider):
    def __init__(self):
        super(MeituanSpider, self).__init__()
        self.ls = list()

    name = 'meituan'
    allowed_domains = ['zz.meituan.com', 'www.meituan.com']
    start_urls = ['http://zz.meituan.com/meishi/']

    def parse(self, response):
        """获取所有的分类，构建所有的分类页面"""
        print("获取到的页面：", response)
        print(response.text)
        data = re.findall("<script>window._appState =(.*?);</script>", response.text)
        print(data)
        data = json.loads(data[0]) if len(data) > 0 else {}
        print(data)
        areas = data.get("filters").get("areas")
        cates = data.get("filters").get("cates")
        # 提取有用数据
        for area in areas:
            area.pop("url")
            area.pop("subAreas")
        for cate in cates:
            cate.pop("url")
        print(areas)
        print(cates)
        area_cate = list()

        for area in areas:
            for cate in cates:
                url = f'http://zz.meituan.com/meishi/c{cate.get("id")}b{area.get("id")}/'
                name = f'{area.get("name")},{cate.get("name")}'
                area_cate.append({"url": url, "name": name})
                print({"url": url, "name": name})
                req = Request(url=url, callback=self.parse_page_count)
                req.headers["Referer"] = f'http://zz.meituan.com/meishi/c{cate.get("id")}/'
                yield req
                break
            break

    def parse_page_count(self, response):
        print("获取到的页面：", response)
        data = re.findall("<script>window._appState =(.*?);</script>", response.text)
        # print(data)
        data = json.loads(data[0]) if len(data) > 0 else {}
        # print(data)
        # count = data.get("poiLists").get("totalCounts")
        poiLists = data.get("poiLists")
        pages = poiLists.get("totalCounts") // 15 + 1 if poiLists else 0
        if not pages:
            req = Request(url=response.request.url, callback=self.parse_page_count)
            # req.headers["Referer"] = f'http://sz.meituan.com/meishi/c{cate.get("id")}/'
            yield req
        else:
            self.ls.append(pages)
            print(f"数据条数为：{len(self.ls)}")
            print(f"页面总数为{pages}")
            item = items.PageUrlItem()
            item["page"] = pages
            item["url"] = response.request.url
            yield item

            for page in range(pages):
                cate_area = response.request.url.split("/")[-2]
                # print(cate_area)
                token = self.get_token()
                page = str(page+1)
                cateId = re.findall("(\d+)", cate_area)[0]
                areaId = re.findall("(\d+)", cate_area)[1]
                referer = response.request.url + f"pn{page}/"
                originUrl = referer.replace('/', '%2F').replace('+', '%2B').replace(':', '%3A')
                cityName = "郑州市"
                # url = f"http://zz.meituan.com/meishi/api/poi/getPoiList?cityName={city}&cateId={cateId}&areaId={areaId}&sort=&dinnerCountAttrId=&page={page}&userId=&uuid=7168142488ce4a8395dd.1566700877.1.0.0&platform=1&partner=126&originUrl={originUrl}&riskLevel=1&optimusCode=10&_token={token}"
                url = 'https://zz.meituan.com/meishi/api/poi/getPoiList?' \
                      'cityName=%s' \
                      '&cateId=%s' \
                      '&areaId=%s' \
                      '&sort=' \
                      '&dinnerCountAttrId=' \
                      '&page=%s' \
                      '&userId=' \
                      '&uuid=05bf3db6-3c2f-41cd-a4ec-ed79ae0a9506' \
                      '&platform=1' \
                      '&partner=126' \
                      '&originUrl=%s' \
                      '&riskLevel=1' \
                      '&optimusCode=1' \
                      '&_token=%s' % (cityName, cateId, areaId, page, originUrl, token)
                # print(url)
                cookies = 'uuid=94fb62e9e2da48eaa76e.1566627630.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=16cc24891aec8-0bc341748ec1f2-7373e61-1fa400-16cc24891afc8; __mta=121429815.1566627631825.1566627631825.1566627639927.2; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1566631212; __utma=211559370.832677555.1566631213.1566631213.1566631213.1; __utmz=211559370.1566631213.1.1.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmcct=zt_search; _lxsdk=16cc24891aec8-0bc341748ec1f2-7373e61-1fa400-16cc24891afc8; ci=73; rvct=73%2C20; _lxsdk_s=16ccb93e625-c43-53c-4a1%7C%7C48'
                req = Request(url=url, callback=self.parse_ids)
                req.headers["Referer"] = referer
                req.headers["cookies"] = cookies
                print("referer:", referer)
                yield req
                break
        # self.area_cate_url_page.append({"url": url, "name": area_cate.get("name"), "area": area_cate.get("area"),
        #                                 "cate": area_cate.get("cate"), "page": page})

    def parse_ids(self, response):
        print(f"获取到的页面：{response}")
        datas = response.text
        print("数据datas:", datas)
        try:
            datas = json.loads(response.text).get("data")
            print(datas)
            if datas:
                datas = datas.get("poiInfos")
            if datas:
                for data in datas:
                    print(f"{data.get('poiId')}:{data.get('title')}")
                    shop_id = data.get("poiId")
                    if shop_id:
                        item = items.IdsItem()
                        item["sid"] = shop_id
                        item["url"] = response.request.url
                        print({"id": shop_id, "url": response.request.url})
                        yield item

                        url = f"https://www.meituan.com/meishi/{shop_id}/"
                        req = Request(url=url, callback=self.parse_store_info)
                        req.headers["Referer"] = url
                        yield req
                        break
        except Exception as e:
            print("发生错误：", e)

    def parse_store_info(self, response):
        # 获取json格式字符串
        shop_info = re.findall("<script>window._appState = (.*?);</script>", response.text)
        # print(shop_info)
        if shop_info:
            try:
                # 去掉最后一个分号，并将数据转换为json
                shop_info = json.loads(shop_info[0]).get("detailInfo")
                # print(shop_info)
            except Exception as e:
                print(e)
                item = items.StoreInfoItem()
                item["name"] = shop_info.get("name")
                item["phone"] = shop_info.get("phone")
                item["address"] = shop_info.get("address")
                item["name"] = shop_info.get("name")
                item["url"] = response.request.url
                print(item)
                yield item

    # 获取token参数
    def get_token(self):
        """获取美团token"""
        ts = int(time.time() * 1000)
        token_dict = {
            'rId': 100900,
            'ver': '1.0.6',
            'ts': ts,
            'cts': ts + 100 * 1000,
            'brVD': [1010, 750],
            'brR': [[1920, 1080], [1920, 1040], 24, 24],
            'bI': ['https://gz.meituan.com/meishi/c11/', ''],
            'mT': [],
            'kT': [],
            'aT': [],
            'tT': [],
            'aM': '',
            'sign': 'eJwdjktOwzAQhu/ShXeJ4zYNKpIXqKtKFTsOMLUn6Yj4ofG4UjkM10CsOE3vgWH36df/2gAjnLwdlAPBBsYoR3J/hYD28f3z+PpUnmJEPqYa5UWEm0mlLBRqOSaP1qjEtFB849VeRXJ51nr56AOSVIi9S0E3LlfSzhitMix/mQwsrdWa7aTyCjInDk1mKu9nvOHauCQWq2rB/8laqd3cX+adv0zdzm3nbjTOdzCi69A/HQAHOOyHafMLmEtKXg=='
        }
        # 二进制编码
        encode = str(token_dict).encode()
        # 二进制压缩
        compress = zlib.compress(encode)
        # base64编码
        b_encode = base64.b64encode(compress)
        # 转为字符串
        token = str(b_encode, encoding='utf-8')
        return token

