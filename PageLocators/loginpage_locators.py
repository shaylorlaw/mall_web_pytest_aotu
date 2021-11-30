# @Time :2021-10-15 17:10
# @Author :ShaylorLaw
# @File :loginpage_locators.py

from selenium.webdriver.common.by import By

class LoginPageLcator:
    #元素定位
    #用户名输入框
    name_text =(By.XPATH,'//input[@id="username"]')
    #密码输入框
    pwd_txt = (By.XPATH,'//input[@id="password"]')
    #登录按钮
    login_but = (By.XPATH,'//button[@class="login-btn login-btn1"]')