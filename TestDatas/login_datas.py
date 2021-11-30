# @Time :2021-10-15 14:23
# @Author :ShaylorLaw
# @File :login_datas.py

#正常场景 -- 测试数据
success_data = {"user":"carisok1046","password":"123456"}

#异常用例 -- 手机格式不正确（大于11位、小于11位、为空、不在号码段），密码有误（错误、为空）
#错误提示都是一种样式，写在一起，不同样式就分开写
wrong_data = [{"user":"188251970940","password":"123456","check":"该用户不存在"},
              {"user":"1882519709","password":"123456","check":"该用户不存在"},
              {"user":"","password":"123456","check":"用户或密码不能为空"},
              {"user":"12220000000","password":"123456","check":"该用户不存在"},
              {"user":"carisok1046","password":"1234567","check":"密码输入错误"},
              {"user":"carisok1046","password":"","check":"用户或密码不能为空"}]