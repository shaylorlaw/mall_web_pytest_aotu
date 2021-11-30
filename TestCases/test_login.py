# @Time :2021-10-13 11:27
# @Author :ShaylorLaw
# @File :test_login.py


from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import login_datas as LD
from TestDatas import common_datas as CD
import ddt
import pytest

class TestLogin:

    # @classmethod
    # def setUpClass(cls):
    #     print("=====所有测试用例之前，setup整个测试类只执行一次=====")
    #     cls.driver=webdriver.Chrome()
    #     cls.driver.get(CD.web_login_url)
    #     cls.lg=LoginPage(cls.driver)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("=====所有测试用例之后，teardown整个测试类只执行一次=====")
    #     cls.driver.quit()
    #
    # def tearDown(self):
    #     self.driver.refresh()

    #放到了conftest中，再调用
    # #每个用例都会执行一次，如果用例之间会互相影响，就用这种方法
    # def setUp(self):
    #     #前置 访问登录页
    #     self.driver=webdriver.Chrome()
    #     self.driver.get(CD.web_login_url)
    #     self.lg = LoginPage(self.driver)
    #
    # def tearDown(self):
    #     #后置
    #     self.driver.quit()

    @pytest.mark.usefixtures("access_web") #在运行的时候，会去运行access_web函数
    @pytest.mark.smoke
    #正常用例 - 登录成功
    def test_login_1_success(self,access_web): #fixture的函数名称作为用例参数，用来接收fixture的返回值
        #步骤 输入用户名 密码 点击登录按钮
        access_web[1].login(LD.success_data["user"],LD.success_data["password"])
        #断言 首页当中 - 能否找到 首页 这个元素
        assert IndexPage(access_web[0]).isExist_Index_ele()

    # 异常用例 -- 手机格式不正确（大于11位、小于11位、为空、不在号码段），密码有误（错误、为空）
    #@ddt.data(*LD.wrong_data)  #pytest.fixture不能用ddt
    @pytest.mark.usefixtures("access_web")  # 在运行的时候，会去运行access_web函数
    @pytest.mark.parametrize("data",LD.wrong_data)
    def test_login_0_wrong(self,data,access_web):
        access_web[1].login(data["user"],data["password"])
        #self.assertEqual(access_web[1].get_errorMsg_from_alert(),data["check"])
        assert access_web[1].get_errorMsg_from_alert() == data["check"]