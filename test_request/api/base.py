import requests


class Base:
    def __init__(self):
        #获取token
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww1cdd06e&corpsecret=R4kEw78I08u9ZQkWQbFOSqgQXYi8TZAXaOrigGVN5sA"
        r = requests.get(url).json()
        self.token = r['access_token']
        #声明一个Session
        self.s = requests.Session()
        #把token放入到session，每次参数都有token
        self.s.params = {'access_token': self.token}

    def send(self, *args, **kwargs):
        #用session
        r = self.s.request(*args, **kwargs)
        return r.json()