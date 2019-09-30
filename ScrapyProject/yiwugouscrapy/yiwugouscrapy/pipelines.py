# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from . import items


class YiwugouscrapyPipeline(object):
    def __init__(self):
        self.kind_count = 0
        self.url_count = 0
        self.info_count = 0

    def process_item(self, item, spider):
        print(item)
        # print("1111111111111111111111111111111111111111111")
        # if isinstance(item, items.AreaUrlscrapyItem):
        #     self.kind_count += 1
        #     print(f"区域种类数：{self.kind_count}")
        #     # print("22222222222222222222222222222222222222")
        #     with open("area_url.json", mode="a", encoding="utf-8") as f:
        #         f.write(json.dumps(dict(item), ensure_ascii=False)+',')
        #
        # elif isinstance(item, items.StoreUrlItem):
        #     self.url_count += 1
        #     print(f"店铺url数：{self.url_count}")
        #     # print("3333333333333333333333333333333333")
        #     with open("store_url.json", mode="a", encoding="utf-8") as f:
        #         f.write(json.dumps(dict(item), ensure_ascii=False)+',')
        #
        # elif isinstance(item, items.StoreInfoItem):
        #     self.info_count += 1
        #     print(f"店铺信息数：{self.info_count}")
        #     # print("444444444444444444444444444444444444")
        #     with open("store_info.json", mode="a", encoding="utf-8") as f:
        #         f.write(json.dumps(dict(item), ensure_ascii=False)+',')
        if isinstance(item, items.StoreInfoItem):
            self.info_count += 1
            print(f"店铺信息数：{self.info_count}")
            # print("444444444444444444444444444444444444")
            with open("store_all_info.json", mode="a", encoding="utf-8") as f:
                f.write(json.dumps(dict(item), ensure_ascii=False)+',')
        elif isinstance(item, items.StoreUrlItem):
            self.url_count += 1
            print(f"店铺url数：{self.url_count}")
            # print("3333333333333333333333333333333333")
            with open("store_url.json", mode="a", encoding="utf-8") as f:
                f.write(json.dumps(dict(item), ensure_ascii=False)+',')
        return item
