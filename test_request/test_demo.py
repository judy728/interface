import json
import requests

class TestDemo:

    #获取token
    def setup(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=1111&corpsecret=2222"
        r = requests.get(url)
        self.token = r.json()['access_token']

    #创建成员
    def test_create(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        body = {
            "userid": "zhang1",
            "name": "张1",
            "mobile": "13356576722",
            "department": [1]
        }
        r = requests.post(url,json=body)
        print(r.json())

    #读取成员
    def test_read(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=111111"
        r = requests.get(url)
        print(r.json())

    #更新成员信息(修改)
    def test_update(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        body = {
            "userid": "linda",
            "name": "沐沐"
        }
        header = {'content-type': 'application/json'}
        r = requests.post(url,data=json.dumps(body),headers=header)
        print(r.json())

    #删除成员
    def test_delete(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=zhang5"
        r = requests.get(url)
        print(r.json())