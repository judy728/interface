import json
import requests


def test_add_member(self):
    #获取token
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww1fb02de4d1cdd06e&corpsecret=R4kEw78I08u9ZQkWQbFOSqgQXYi8TZAXaOrigGVN5sA"
    r = requests.get(url)
    token = r.json()['access_token']

    #数据清理（删除成员）
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhang5"
    r = requests.get(url)
    print(r.json())

    #创建成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {
        "userid": "花花",
        "name": "花花",
        "mobile": "13356270099",
        "department": [1]
    }
    r = requests.post(url, json=body)
    # print(r.json())

    #读取成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=花花"
    r = requests.get(url)
    print(r.json())

def test_delete_member(self):
    # 获取token
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww1fb02de4d1cdd06e&corpsecret=R4kEw78I08u9ZQkWQbFOSqgQXYi8TZAXaOrigGVN5sA"
    r = requests.get(url)
    token = r.json()['access_token']

    #数据清理（数据准备）
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {
        "userid": "花花",
        "name": "花花",
        "mobile": "13356270099",
        "department": [1]
    }
    r = requests.post(url, json=body)

    #删除成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhang5"
    r = requests.get(url)
    print(r.json())

    # 读取成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=花花"
    r = requests.get(url)
    # print(r.json())