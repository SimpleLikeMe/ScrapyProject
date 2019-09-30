import requests
import base64
from fontTools.ttLib import TTFont
import re
from PIL import Image, ImageDraw, ImageFont


def get_phone():
    maps = list()
    phone_num = "0393-8557337"
    url = "https://tdabingjixiea3.cn.china.cn/"
    # headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Cookie': '_lxsdk_cuid=16d1fd74354c8-00202564da26bf-5373e62-1fa400-16d1fd74354c8; _lxsdk=16d1fd74354c8-00202564da26bf-5373e62-1fa400-16d1fd74354c8; _hc.v=d0488bc3-1184-0b5e-28f4-1e5a5baa5905.1568197264; cy=160; cye=zhengzhou; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; s_ViewType=10; _lxsdk_s=16d393d378f-5c0-8a1-641%7C%7C50', 'Host': 'www.dianping.com', 'If-Modified-Since': 'Sat, 14 Sep 2019 16:43:22 GMT', 'If-None-Match': '"169c9917a61d082ef33c1d5aafd3566a"', 'Referer': 'http://www.dianping.com/zhengzhou/ch10/g110', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    # html = requests.get(url=url, headers=headers)
    html = requests.get(url=url)
    print(html.text)
    html = html.text
    base64_string = html.split("base64,")[1].split("'")[0]
    bin_data = base64.decodebytes(base64_string.encode())
    print(bin_data)
    with open("base.woff", r"wb") as f:
        f.write(bin_data)

    phone = re.findall('<span class="secret">(.*?)</span>', html)
    font_list = re.findall('&#x(\w+)', phone[0])
    print(font_list)
    font_list = re.findall('&#x(\w+)', phone[1])
    print(font_list)
    font_list = re.findall('&#x(\w+)', phone[2])
    print(font_list)
    for font_secret in font_list:
        one_font = int(font_secret, 16)
        font = TTFont('base.woff')
        font.saveXML('test3.xml')
        c = font['cmap']
        d = c.tables[1]
        e = d.ttFont
        f = e.tables['cmap']
        g = f.tables[1]
        h = g.cmap
        # print("c::::::", c)
        gly_font = h[one_font]
        b = font['cmap'].tables[0].ttFont.getReverseGlyphMap()
        # print("b:::::::", b)
        print(b[gly_font] - 1, end="")
        break

    z = zip(font_list, list(phone_num))
    print(list(phone_num))
    ls = list()
    for i in z:
        ls.append(i)

    with open("test3.xml", mode="r", encoding="utf-8") as f:
        data = f.read()
    lis = re.findall('<CharStringname=".*?">.*?</CharString>', re.sub("\s", "", data))
    keys = list()
    for li in lis:
        key = re.findall('<CharStringname="(.*?)">', li)
        if not len(key):
            continue
        key = re.sub("uni", "", key[0])
        keys.append(key)
        value = re.findall('<CharStringname.*?>(.*?)<.*?>', li)
        if not len(value):
            continue
        value = value[0]
        for i in ls:
            if i[0] == key:
                d = (i[1], value)
                maps.append(d)
        print(key, ":", value)
    d1 = {'126983rmoveto-680rlineto07rlineto160rlineto503307rrcurveto00rlineto0134rlineto06-22-5-3rrcurveto00rlineto-16-8rlineto-38rlineto3922rlineto7-4rlineto0-157rlineto0-73-350rrcurveto00rlineto160rlineto0-7rlinetoendchar': '1', '1263984rmoveto00rlineto-28rlineto28101415-119rrcurveto00rlineto016-78-130rrcurveto00rlineto-151-14-10-13-20rrcurveto00rlineto-63rlineto11311716231rrcurveto00rlineto26-113-121-24rrcurveto00rlineto0-15-9-13-17-12rrcurveto00rlineto25-312-150-26rrcurveto00rlineto-2-39-24-20-47-2rrcurveto00rlineto-181-95-19rrcurveto00rlineto173461rrcurveto00rlineto305-37-5rrcurveto00rlineto-11102-1rrcurveto00rlineto7-56-250rrcurveto00rlineto1931014225rrcurveto00rlineto331-1711-37-8rrcurvetoendchar': '3', '12611177rmoveto1010rlineto0-6rlineto-53-172rlineto-210rlineto52157rlineto-560rlineto-61-3-3-1-6rrcurveto00rlineto-7-22rlineto-60rlineto051rlinetoendchar': '7', '12610656rmoveto60rlineto0-53rlineto-1040rlineto07rlineto4755rlineto1720821023rrcurveto00rlineto021-810-170rrcurveto00rlineto-151-13-12-12-24rrcurveto00rlineto-72rlineto9361818260rrcurveto00rlineto28-215-161-30rrcurveto00rlineto1-18-11-21-23-25rrcurveto00rlineto-39-44rlineto520rlineto11-1710322rrcurveto00rlinetoendchar': '2', '12663173rmoveto00rlineto-211-11-280-56rrcurveto00rlineto-1-5811-28222rrcurveto00rlineto22-11128-157rrcurveto00rlineto056-1128-21-1rrcurveto08rmoveto00rlineto33-419-305-57rrcurveto00rlineto-3-57-19-30-35-3rrcurveto00rlineto-352-1930-259rrcurveto00rlineto4571930333rrcurvetoendchar': '0', '12615-1rmoveto00rlineto-27rlineto43152525735rrcurveto00rlineto-11-11-12-6-130rrcurveto00rlineto-273-1518-233rrcurveto00rlineto1411721331rrcurveto00rlineto35-118-251-49rrcurveto00rlineto0-59-33-36-66-12rrcurveto7595rmoveto00rlineto253-1026-22-1rrcurveto00rlineto-190-9-160-32rrcurveto00rlineto-1-3310-16211rrcurveto00rlineto11196811rrcurvetoendchar': '9', '12698156rmoveto-590rlineto-8-36rlineto50125-211-42rrcurveto00rlineto-3-37-22-20-42-3rrcurveto00rlineto-200-105-19rrcurveto00rlineto083470rrcurveto00rlineto516-38-7rrcurveto00rlineto8-56-330rrcurveto00rlineto171914126rrcurveto00rlineto232-2015-42-1rrcurveto00rlineto-30-1203rrcurveto00rlineto1577rlineto740rlineto-4-16rlineto0-3-2-2-30rrcurveto00rlinetoendchar': '5', '126111181rmoveto00rlineto0-8rlineto-43-12-25-25-7-39rrcurveto00rlineto109115120rrcurveto00rlineto29-216-182-34rrcurveto00rlineto-3-35-18-19-33-3rrcurveto00rlineto-351-1823-145rrcurveto00rlineto56334376312rrcurveto-50-85rmoveto00rlineto-90-9-3-9-6rrcurveto00rlineto-1-120-91-7rrcurveto00rlineto1-3610-18191rrcurveto00rlineto1911015030rrcurveto00rlineto130-1115-22-1rrcurvetoendchar': '6', '1269460rmoveto250rlineto0-20rlineto-250rlineto0-41rlineto-200rlineto041rlineto-700rlineto019rlineto78122rlineto120rlineto0-121rlineto-790rmoveto590rlineto092rlineto-59-92rlinetoendchar': '4', '1265483rmoveto00rlineto-16-11-8-131-15rrcurveto00rlineto1-2311-1221-1rrcurveto00rlineto1921011119rrcurveto00rlineto015-1415-2715rrcurveto8-84rmoveto00rlineto-312-1714-325rrcurveto00rlineto-11811172315rrcurveto00rlineto-2114-1016118rrcurveto00rlineto2271514292rrcurveto00rlineto27-215-132-24rrcurveto00rlineto1-16-10-14-21-13rrcurveto00rlineto27-1513-18-1-22rrcurveto00rlineto-1-29-17-15-33-1rrcurveto-27148rmoveto00rlineto-1-1410-1421-14rrcurveto00rlineto1512813014rrcurveto00rlineto-118-1010-191rrcurveto00rlineto-15-1-8-9-1-16rrcurvetoendchar': '8'}
    # d1 = {'126983rmoveto-680rlineto07rlineto160rlineto503307rrcurveto00rlineto0134rlineto06-22-5-3rrcurveto00rlineto-16-8rlineto-38rlineto3922rlineto7-4rlineto0-157rlineto0-73-350rrcurveto00rlineto160rlineto0-7rlinetoendchar': '1', '1263984rmoveto00rlineto-28rlineto28101415-119rrcurveto00rlineto016-78-130rrcurveto00rlineto-151-14-10-13-20rrcurveto00rlineto-63rlineto11311716231rrcurveto00rlineto26-113-121-24rrcurveto00rlineto0-15-9-13-17-12rrcurveto00rlineto25-312-150-26rrcurveto00rlineto-2-39-24-20-47-2rrcurveto00rlineto-181-95-19rrcurveto00rlineto173461rrcurveto00rlineto305-37-5rrcurveto00rlineto-11102-1rrcurveto00rlineto7-56-250rrcurveto00rlineto1931014225rrcurveto00rlineto331-1711-37-8rrcurvetoendchar': '3', '12611177rmoveto1010rlineto0-6rlineto-53-172rlineto-210rlineto52157rlineto-560rlineto-61-3-3-1-6rrcurveto00rlineto-7-22rlineto-60rlineto051rlinetoendchar': '7', '12610656rmoveto60rlineto0-53rlineto-1040rlineto07rlineto4755rlineto1720821023rrcurveto00rlineto021-810-170rrcurveto00rlineto-151-13-12-12-24rrcurveto00rlineto-72rlineto9361818260rrcurveto00rlineto28-215-161-30rrcurveto00rlineto1-18-11-21-23-25rrcurveto00rlineto-39-44rlineto520rlineto11-1710322rrcurveto00rlinetoendchar': '2', '12663173rmoveto00rlineto-211-11-280-56rrcurveto00rlineto-1-5811-28222rrcurveto00rlineto22-11128-157rrcurveto00rlineto056-1128-21-1rrcurveto08rmoveto00rlineto33-419-305-57rrcurveto00rlineto-3-57-19-30-35-3rrcurveto00rlineto-352-1930-259rrcurveto00rlineto4571930333rrcurvetoendchar': '0', '12615-1rmoveto00rlineto-27rlineto43152525735rrcurveto00rlineto-11-11-12-6-130rrcurveto00rlineto-273-1518-233rrcurveto00rlineto1411721331rrcurveto00rlineto35-118-251-49rrcurveto00rlineto0-59-33-36-66-12rrcurveto7595rmoveto00rlineto253-1026-22-1rrcurveto00rlineto-190-9-160-32rrcurveto00rlineto-1-3310-16211rrcurveto00rlineto11196811rrcurvetoendchar': '9', '12698156rmoveto-590rlineto-8-36rlineto50125-211-42rrcurveto00rlineto-3-37-22-20-42-3rrcurveto00rlineto-200-105-19rrcurveto00rlineto083470rrcurveto00rlineto516-38-7rrcurveto00rlineto8-56-330rrcurveto00rlineto171914126rrcurveto00rlineto232-2015-42-1rrcurveto00rlineto-30-1203rrcurveto00rlineto1577rlineto740rlineto-4-16rlineto0-3-2-2-30rrcurveto00rlinetoendchar': '5', '126111181rmoveto00rlineto0-8rlineto-43-12-25-25-7-39rrcurveto00rlineto109115120rrcurveto00rlineto29-216-182-34rrcurveto00rlineto-3-35-18-19-33-3rrcurveto00rlineto-351-1823-145rrcurveto00rlineto56334376312rrcurveto-50-85rmoveto00rlineto-90-9-3-9-6rrcurveto00rlineto-1-120-91-7rrcurveto00rlineto1-3610-18191rrcurveto00rlineto1911015030rrcurveto00rlineto130-1115-22-1rrcurvetoendchar': '6', '1269460rmoveto250rlineto0-20rlineto-250rlineto0-41rlineto-200rlineto041rlineto-700rlineto019rlineto78122rlineto120rlineto0-121rlineto-790rmoveto590rlineto092rlineto-59-92rlinetoendchar': '4', '1265483rmoveto00rlineto-16-11-8-131-15rrcurveto00rlineto1-2311-1221-1rrcurveto00rlineto1921011119rrcurveto00rlineto015-1415-2715rrcurveto8-84rmoveto00rlineto-312-1714-325rrcurveto00rlineto-11811172315rrcurveto00rlineto-2114-1016118rrcurveto00rlineto2271514292rrcurveto00rlineto27-215-132-24rrcurveto00rlineto1-16-10-14-21-13rrcurveto00rlineto27-1513-18-1-22rrcurveto00rlineto-1-29-17-15-33-1rrcurveto-27148rmoveto00rlineto-1-1410-1421-14rrcurveto00rlineto1512813014rrcurveto00rlineto-118-1010-191rrcurveto00rlineto-15-1-8-9-1-16rrcurvetoendchar': '8'}
    for i in maps:

        d1[i[1]] = i[0]
        # print(i)
    print(d1)
    print(d1.values())






# get_phone()
d = {'126983rmoveto-680rlineto07rlineto160rlineto503307rrcurveto00rlineto0134rlineto06-22-5-3rrcurveto00rlineto-16-8rlineto-38rlineto3922rlineto7-4rlineto0-157rlineto0-73-350rrcurveto00rlineto160rlineto0-7rlinetoendchar': '1', '1263984rmoveto00rlineto-28rlineto28101415-119rrcurveto00rlineto016-78-130rrcurveto00rlineto-151-14-10-13-20rrcurveto00rlineto-63rlineto11311716231rrcurveto00rlineto26-113-121-24rrcurveto00rlineto0-15-9-13-17-12rrcurveto00rlineto25-312-150-26rrcurveto00rlineto-2-39-24-20-47-2rrcurveto00rlineto-181-95-19rrcurveto00rlineto173461rrcurveto00rlineto305-37-5rrcurveto00rlineto-11102-1rrcurveto00rlineto7-56-250rrcurveto00rlineto1931014225rrcurveto00rlineto331-1711-37-8rrcurvetoendchar': '3', '12611177rmoveto1010rlineto0-6rlineto-53-172rlineto-210rlineto52157rlineto-560rlineto-61-3-3-1-6rrcurveto00rlineto-7-22rlineto-60rlineto051rlinetoendchar': '7', '12610656rmoveto60rlineto0-53rlineto-1040rlineto07rlineto4755rlineto1720821023rrcurveto00rlineto021-810-170rrcurveto00rlineto-151-13-12-12-24rrcurveto00rlineto-72rlineto9361818260rrcurveto00rlineto28-215-161-30rrcurveto00rlineto1-18-11-21-23-25rrcurveto00rlineto-39-44rlineto520rlineto11-1710322rrcurveto00rlinetoendchar': '2', '12663173rmoveto00rlineto-211-11-280-56rrcurveto00rlineto-1-5811-28222rrcurveto00rlineto22-11128-157rrcurveto00rlineto056-1128-21-1rrcurveto08rmoveto00rlineto33-419-305-57rrcurveto00rlineto-3-57-19-30-35-3rrcurveto00rlineto-352-1930-259rrcurveto00rlineto4571930333rrcurvetoendchar': '0', '12615-1rmoveto00rlineto-27rlineto43152525735rrcurveto00rlineto-11-11-12-6-130rrcurveto00rlineto-273-1518-233rrcurveto00rlineto1411721331rrcurveto00rlineto35-118-251-49rrcurveto00rlineto0-59-33-36-66-12rrcurveto7595rmoveto00rlineto253-1026-22-1rrcurveto00rlineto-190-9-160-32rrcurveto00rlineto-1-3310-16211rrcurveto00rlineto11196811rrcurvetoendchar': '9', '12698156rmoveto-590rlineto-8-36rlineto50125-211-42rrcurveto00rlineto-3-37-22-20-42-3rrcurveto00rlineto-200-105-19rrcurveto00rlineto083470rrcurveto00rlineto516-38-7rrcurveto00rlineto8-56-330rrcurveto00rlineto171914126rrcurveto00rlineto232-2015-42-1rrcurveto00rlineto-30-1203rrcurveto00rlineto1577rlineto740rlineto-4-16rlineto0-3-2-2-30rrcurveto00rlinetoendchar': '5', '126111181rmoveto00rlineto0-8rlineto-43-12-25-25-7-39rrcurveto00rlineto109115120rrcurveto00rlineto29-216-182-34rrcurveto00rlineto-3-35-18-19-33-3rrcurveto00rlineto-351-1823-145rrcurveto00rlineto56334376312rrcurveto-50-85rmoveto00rlineto-90-9-3-9-6rrcurveto00rlineto-1-120-91-7rrcurveto00rlineto1-3610-18191rrcurveto00rlineto1911015030rrcurveto00rlineto130-1115-22-1rrcurvetoendchar': '6', '1269460rmoveto250rlineto0-20rlineto-250rlineto0-41rlineto-200rlineto041rlineto-700rlineto019rlineto78122rlineto120rlineto0-121rlineto-790rmoveto590rlineto092rlineto-59-92rlinetoendchar': '4', '1265483rmoveto00rlineto-16-11-8-131-15rrcurveto00rlineto1-2311-1221-1rrcurveto00rlineto1921011119rrcurveto00rlineto015-1415-2715rrcurveto8-84rmoveto00rlineto-312-1714-325rrcurveto00rlineto-11811172315rrcurveto00rlineto-2114-1016118rrcurveto00rlineto2271514292rrcurveto00rlineto27-215-132-24rrcurveto00rlineto1-16-10-14-21-13rrcurveto00rlineto27-1513-18-1-22rrcurveto00rlineto-1-29-17-15-33-1rrcurveto-27148rmoveto00rlineto-1-1410-1421-14rrcurveto00rlineto1512813014rrcurveto00rlineto-118-1010-191rrcurveto00rlineto-15-1-8-9-1-16rrcurvetoendchar': '8', '14012694rmoveto0-17rlineto-1130rlineto017rlineto1130rlinetoendchar': '-'}
# for i in d1.keys():
#     print(d.get(i))

import re
from fontTools.ttLib import TTFont

font = TTFont('base.woff') #打开本地的ttf文件
bestcmap = font['cmap'].getBestCmap()
newmap = dict()
for key in bestcmap.keys():
    value = int(re.search(r'(\d+)', bestcmap[key]).group(1)) - 1
    key = hex(key)
    newmap[key] = value
print(newmap)
