
def insert():
    import json
    from redis import Redis
    from urllib import parse

    # 获取redis连接对象
    redis = Redis(host="114.116.126.177", password="jiefutong")
    # redis = Redis()
    with open("kind.json", mode="r", encoding="utf-8") as f:
        datas = json.loads(f.read())

    for data in datas:
        print(data)
        redis.lpush("lbw:start_urls", f'http://b2b.liebiao.com/sou-gs/{data}/?pn=1')

    # 关闭redis
    redis.close()


def init_search():
    import json
    import re

    with open("kinds.json", mode="r", encoding="utf-8") as f:
        datas = json.loads(f.read())

    ls = list()
    for data in datas:
        ls.append(re.sub("市场", "", data[0]))
        for i in data[1]:
            print(i)
            ls.append(re.sub("\W", "", i))

    print(ls)
    print(len(ls))
    with open("kind.json", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(ls, ensure_ascii=False))

    with open("area_url.json", mode="r", encoding="utf-8") as f:
        datas = json.loads(f.read())
    ls1 = list()

    for data in datas:
        print(data.get("kind"))
        ls1.append(re.sub("\W", "", data.get("kind")))

    print(ls1)
    print(len(ls1))

    with open("kind1.json", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(ls, ensure_ascii=False))

    with open("kind2.json", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(ls.extend(ls1), ensure_ascii=False))



if __name__ == '__main__':
    # init_search()
    insert()
