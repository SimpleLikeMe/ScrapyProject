import json
from urllib import parse
from redis import StrictRedis

# 使用默认方式连接到数据库
redis = StrictRedis(host='localhost', port=6379, db=0)

with open("kind_city.json", mode="r", encoding="utf-8") as f:
    datas = json.loads(f.read())

url1 = "https://s.1688.com/company/company_search.htm?"
for data in datas:
    province = data.get("province")
    city = data.get("city")
    keywords = data.get("kind")
    params = {
        "province": province.encode('GBK'),
        "city": city.encode('GBK'),
        "keywords": keywords.encode('GBK'),
        "n": "y",
        "filt": "y",
    }
    params = parse.urlencode(params)
    url = f"https://s.1688.com/company/company_search.htm?{params}"
    print(url)
    # 插入数据
    redis.lpush("alibaba:start_urls", url)
    # break

print(len(datas))
# 关闭连接
redis.close()


