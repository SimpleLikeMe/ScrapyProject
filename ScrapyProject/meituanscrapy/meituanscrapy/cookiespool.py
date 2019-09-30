import requests


def get_cookie():
    return requests.get("http://127.0.0.1:5000/meituan/random").json()


if __name__ == '__main__':
    print(get_cookie())
    print(get_cookie())
    print(get_cookie())
    print(get_cookie())
    print(get_cookie())