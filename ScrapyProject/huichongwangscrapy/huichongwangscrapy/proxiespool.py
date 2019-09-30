import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

# your spider code

def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy().get("proxy")
    while retry_count > 0:
        try:
            html = requests.get('https://www.example.com', proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    delete_proxy(proxy)
    return None

def str_to_dict(s):
    print({i.split(":")[0]: i.split(":")[1] for i in s.split("\n")})
    try:
        print({i.split(": ")[0]: i.split(": ")[1] for i in s.split("\n")})
    except Exception as e:
        print(e)

if __name__ == '__main__':
    print(get_proxy())
    print(get_proxy())
    print(get_proxy())
    print(get_proxy())
    print(get_proxy())
    s = """Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding:gzip, deflate, br
Accept-Language:zh-CN,zh;q=0.9
Cache-Control:max-age=0
Connection:keep-alive
Cookie:_lxsdk_cuid=16cada1b7f4c8-0f89af9fae9044-3c604504-1fa400-16cada1b7f44f; ci=73; _hc.v=7b13c0c8-68fe-2abe-1d09-775242b3f19c.1566283093; uuid=b5b1261edc284650b230.1566621472.1.0.0; _lx_utm=utm_source%3Dso.com%26utm_medium%3Dorganic; __mta=108886077.1566363379828.1566363379828.1566621474088.2; client-id=b0a4af80-6822-4e6d-b325-53882aa6b4a8; _lxsdk_s=16cc1ea9a78-9b-cf6-6dc%7C%7C4
Host:zz.meituan.com
Referer:http://zz.meituan.com/
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"""

    str_to_dict(s)
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Cookie': '_lxsdk_cuid=16cada1b7f4c8-0f89af9fae9044-3c604504-1fa400-16cada1b7f44f; ci=73; _hc.v=7b13c0c8-68fe-2abe-1d09-775242b3f19c.1566283093; uuid=b5b1261edc284650b230.1566621472.1.0.0; _lx_utm=utm_source%3Dso.com%26utm_medium%3Dorganic; __mta=108886077.1566363379828.1566363379828.1566621474088.2; client-id=b0a4af80-6822-4e6d-b325-53882aa6b4a8; _lxsdk_s=16cc1ea9a78-9b-cf6-6dc%7C%7C4', 'Host': 'zz.meituan.com', 'Referer': 'http', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

