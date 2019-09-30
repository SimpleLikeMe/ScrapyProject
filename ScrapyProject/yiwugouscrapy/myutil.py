import json
import pandas as pd

def read_data():
    ls = list()
    with open("./store_url1.json", mode="r", encoding="utf-8") as f:
        datas = json.loads("["+f.read()[:-1]+"]")
        print(len(datas))
    for d in datas:
        if d not in ls:
            ls.append(d)
    print(len(ls))
    # with open("./store_url2.json", mode="w", encoding="utf-8") as f:
    #     f.write(json.dumps(ls, ensure_ascii=False))


def split_file():
    with open("./store_info.json", mode="r", encoding="utf-8") as f:
        datas = json.loads("["+f.read()[:-1]+"]")

    ls = datas[0:]
    print(len(ls))

    # with open("data\page_url1.json", mode="w", encoding="utf-8") as f:
    #     f.write(json.dumps(ls))


def merger_file():
    ls = list()
    for i in range(5):
        with open(f"data\store_detail{i+1}.json", mode="r", encoding="utf-8") as f:
            datas = json.loads(f.read())
            ls.extend(datas)
    ls1 = list()
    for i in ls:
        if i not in ls1:
            ls1.append(i)
    print(len(ls1))
    print(ls)
    # print(pd.read_json(f"data\store_info_duplicated.json"))
    df = pd.DataFrame(ls)
    print(df)
    # print(df['phone'].duplicated())
    bl = df.drop_duplicates()
    bl.to_csv("data\store_ids_duplicated.csv", encoding="utf-8")
    bl.to_json("data\store_ids_duplicated.json")
    print(bl)
    # with open(f"data\store_info_duplicated.json", mode="r", encoding="utf-8") as f:
    #     d = json.loads(f.read())
    #     print(d)
    #     print(type(d))

    with open("data\郑州\store_detail.json", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(ls1, ensure_ascii=False))


def quchong():
    # 去重 .duplicated()
    # datas = [1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 5]
    # # 获取Series对象
    # s = pd.Series(datas)
    # # 获取重复的数据索引
    # print(s.duplicated(keep='first'))
    # # 获取不重复的数据索引
    # print(s[s.duplicated() == False])
    # print('-----')
    # # 判断是否重复
    # # 通过布尔判断，得到不重复的值

    # 获取不重复的数据
    # s_re = s.drop_duplicates()
    # print(s_re)
    # print('-----')
    # drop.duplicates移除重复
    # inplace参数：是否替换原值，默认False

    # df = pd.DataFrame({'key1': ['a', 'a', 3, 4, 5],
    #                    'key2': ['a', 'a', 'b', 'b', 'c']})
    # print(df)
    # print(df.duplicated())  # 判断行是否重复
    # print(df['key2'].duplicated())  # 当指定某列时，等同于Series去重
    # Dataframe中使用duplicated
    data = [{'name': '韩风源自助烤肉（国贸精品直营店）', 'phone': '0371', 'address': '金水区花园路与丰产路交叉口向西50米路南（新世纪大厦停车场、关虎屯丹尼斯生活停车场下车步行即到）', 'area': 166, 'cate': 40}, {'name': '厚道寿喜烧日式火锅料理（东风路店）', 'phone': '0371', 'address': '金水区东风路与信息学院路交叉口向西100米路北财智名座20楼2017', 'area': 166, 'cate': 40}]
    data1 = [{"name":"ddd", "phone":"222"}, {"name":"ddd", "phone":"222"}]
    df = pd.DataFrame(data1)
    print(df)
    print(df['phone'].duplicated())
    bl = df.drop_duplicates(["phone", "name"])
    print(bl)

if __name__ == '__main__':
    # split_file()
    # merger_file()
    # quchong()
    read_data()