# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from . import items

class MeituanscrapyPipeline(object):
    def process_item(self, item, spider):
        print("pipeline:", item)
        if isinstance(item, items.PageUrlItem):
            with open("page.json", mode="a", encoding="utf-8") as f:
                f.write(json.dumps(dict(item), ensure_ascii=False) + ",")
            return item
        elif isinstance(item, items.IdsItem):
            with open("ids.json", mode="a", encoding="utf-8") as f:
                f.write(json.dumps(dict(item), ensure_ascii=False) + ",")
            return item

        elif isinstance(item, items.StoreInfoItem):
            with open("store_info.json", mode="a", encoding="utf-8") as f:
                f.write(json.dumps(dict(item), ensure_ascii=False) + ",")
            return item
