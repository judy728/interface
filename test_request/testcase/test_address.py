import pytest
from test_request.api.address import Address

class TestAddress:
    def setup(self):
        self.address = Address()

    @pytest.mark.parametrize("userid, mobile",[("sasa","13567767700"),
                                               ("li","13566777701"),
                                               ("li","13536777702")])
    def test_add_member(self, userid, mobile):
        name = "陌陌"
        department = [1]
        #数据清理
        self.address.delete_member(userid)
        #创建成员
        r = self.address.add_member(userid=userid, name=name, mobile=mobile, department=department)
        assert r.get("errcode") == 0
        #查询结果
        r = self.address.get_member(userid)
        assert r.get("name", "userid 添加失败") == name