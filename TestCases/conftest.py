# @Time :2021-11-24 10:36
# @Author :ShaylorLaw
# @File :conftest.py

import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from TestDatas import common_datas as CD

driver = None

#声明它是一个fixture
#@pytest.fixture(scope="class")
@pytest.fixture
def access_web():
    global driver
    print("=====每个用例开始执行一次=====")
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    lg = LoginPage(driver)
    yield (driver,lg) #分隔线；后面接返回值
    #后置操作
    print("=====每个用例结束执行一次=====")
    driver.quit()