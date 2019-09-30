import requests
import base64
from fontTools.ttLib import TTFont
import re


def parse_detail(html):
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
    # 获取base64加密的字体
    base64_string = html.split("base64,")[1].split("'")[0]
    # 使用base64库对加密字体进行解码
    bin_data = base64.decodebytes(base64_string.encode())
    # 将字体保存到本地
    with open(f"./fonts/{base64_string[:30]}.woff", r"wb") as f:
        f.write(bin_data)
    # 使用TTFont打开文件
    font = TTFont(f"./fonts/{base64_string[:30]}.woff")
    # 将文件保存为xml格式
    font.saveXML(f"./fonts/{base64_string[:30]}.xml")

    # 打开保存的xml字体关系映射表
    with open(f"./fonts/{base64_string[:30]}.xml", mode="r", encoding="utf-8") as f:
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
    return phone


# url = "https://tdabingjixiea3.cn.china.cn/"
# html = requests.get(url=url)
# # print(html.text)
# html = html.text
# phone = parse_detail(html)
# print(phone)


k = "%E6%99%BA%E8%83%BD%E8%AE%BE%E5%A4%87"
""""
    $.ajax({
      type: 'POST',
      url: '/common/search.php',
      data: 'key=' + b + '&entType=' + a,
      async: !0,
      dataType: 'json',
      timeout: '5000',
"""
'{"url":"https://product.cn.china.cn/suppliers/%E6%99%BA%E8%83%BD%E8%AE%BE%E5%A4%87/"}'
data1 = "key=%E6%99%BA%E8%83%BD%E8%AE%BE%E5%A4%87&entType=1"
headers = {'Host': 'cn.china.cn',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'Accept-Encoding': 'gzip, deflate, br', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'X-Requested-With': 'XMLHttpRequest', 'Content-Length': '50', 'Connection': 'keep-alive',
           'Referer': 'https://cn.china.cn/',
           'Cookie': 'Hm_lvt_3cfaa114cca90dbeb8cf6908074f92ef=1568699355,1568705573,1568708511,1568708523; Hm_lvt_066cf190c4bdf8653ad5ea8f496c4a13=1568773166,1568773175,1568773187,1568773313; china_uv=718fc9b75bcbe8e9ddfe06ed1c702fa5; Hm_lvt_6633f2c221756b56fb625ded6d946372=1568687092; SMTKF_visitor_id_39034=212647152; BAIDU_SSP_lcr=https://www.baidu.com/link?url=8G7P1-9LCKbqeytFDS73KnIIWqt8mupcoZgOUtnk7jm&wd=&eqid=8d59b3fc001c0990000000035d818d17; Hm_lpvt_066cf190c4bdf8653ad5ea8f496c4a13=1568773313; search-token=80b40c95efc6e5df46eae76d26fe9ca6',
           'Cache-Control': 'max-age=0', 'TE': 'Trailers'}
# url = "https://cn.china.cn/common/search.php"
# data = {"key": "智能设备", "entType": "1"}
# res = requests.post(url=url, headers=headers, data=data)
# print(res.text)
# print(res.status_code)
# print(url)
# url = res.json().get("url")
headers = {'Host': 'www.china.cn', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2', 'Accept-Encoding': 'gzip, deflate, br', 'Referer': 'https://product.cn.china.cn/suppliers/%E6%99%BA%E8%83%BD%E8%AE%BE%E5%A4%87/', 'Connection': 'keep-alive', 'Cookie': 'Hm_lvt_60030dce41abe35fdcca4338a88126a7=1568772827,1568773090,1568773173,1568773183; Hm_lvt_066cf190c4bdf8653ad5ea8f496c4a13=1568773166,1568773175,1568773187,1568773313; china_uv=718fc9b75bcbe8e9ddfe06ed1c702fa5; Hm_lvt_6633f2c221756b56fb625ded6d946372=1568687092; SMTKF_visitor_id_39034=212647152; Hm_lvt_eacc334f8eb162234e4fc886d62315dc=1568710235; BAIDU_SSP_lcr=https://www.baidu.com/link?url=8G7P1-9LCKbqeytFDS73KnIIWqt8mupcoZgOUtnk7jm&wd=&eqid=8d59b3fc001c0990000000035d818d17; Hm_lpvt_066cf190c4bdf8653ad5ea8f496c4a13=1568773931; PHPSESSID=d732eb5b6e11ef5f57b7b95bdbff12a7; Hm_lpvt_60030dce41abe35fdcca4338a88126a7=1568773941', 'Upgrade-Insecure-Requests': '1', 'Cache-Control': 'max-age=0', 'TE': 'Trailers'}
# res = requests.get(url=url, headers=headers)
# res = requests.get(url=url)
#
# print(res.text)
# url = "https://product.cn.china.cn/suppliers/%E6%99%BA%E8%83%BD%E8%AE%BE%E5%A4%87/"
# res = requests.get(url=url, headers=headers)
# print(res.text)


url = "https://cn.china.cn/common/spider.php?v=60404"
res = requests.post(url=url, headers=headers)
print(res.text)
print(res.status_code)

s = """Host: cn.china.cn
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 50
Connection: keep-alive
Referer: https://cn.china.cn/
Cookie: Hm_lvt_3cfaa114cca90dbeb8cf6908074f92ef=1568699355,1568705573,1568708511,1568708523; Hm_lvt_066cf190c4bdf8653ad5ea8f496c4a13=1568773166,1568773175,1568773187,1568773313; china_uv=718fc9b75bcbe8e9ddfe06ed1c702fa5; Hm_lvt_6633f2c221756b56fb625ded6d946372=1568687092; SMTKF_visitor_id_39034=212647152; BAIDU_SSP_lcr=https://www.baidu.com/link?url=8G7P1-9LCKbqeytFDS73KnIIWqt8mupcoZgOUtnk7jm&wd=&eqid=8d59b3fc001c0990000000035d818d17; Hm_lpvt_066cf190c4bdf8653ad5ea8f496c4a13=1568773313; search-token=80b40c95efc6e5df46eae76d26fe9ca6
Cache-Control: max-age=0
TE: Trailers"""
s = """Host: www.china.cn
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Referer: https://product.cn.china.cn/suppliers/%E6%99%BA%E8%83%BD%E8%AE%BE%E5%A4%87/
Connection: keep-alive
Cookie: Hm_lvt_60030dce41abe35fdcca4338a88126a7=1568772827,1568773090,1568773173,1568773183; Hm_lvt_066cf190c4bdf8653ad5ea8f496c4a13=1568773166,1568773175,1568773187,1568773313; china_uv=718fc9b75bcbe8e9ddfe06ed1c702fa5; Hm_lvt_6633f2c221756b56fb625ded6d946372=1568687092; SMTKF_visitor_id_39034=212647152; Hm_lvt_eacc334f8eb162234e4fc886d62315dc=1568710235; BAIDU_SSP_lcr=https://www.baidu.com/link?url=8G7P1-9LCKbqeytFDS73KnIIWqt8mupcoZgOUtnk7jm&wd=&eqid=8d59b3fc001c0990000000035d818d17; Hm_lpvt_066cf190c4bdf8653ad5ea8f496c4a13=1568773931; PHPSESSID=d732eb5b6e11ef5f57b7b95bdbff12a7; Hm_lpvt_60030dce41abe35fdcca4338a88126a7=1568773941
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
TE: Trailers"""
print({i.split(": ")[0]: i.split(": ")[1] for i in s.split("\n")})
