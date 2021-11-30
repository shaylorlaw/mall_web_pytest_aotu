# @Time :2021-10-13 11:27
# @Author :ShaylorLaw
# @File :login_page.py

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.loginpage_locators import LoginPageLcator
from Common.basepage import BasePage

class LoginPage(BasePage):

    # def __init__(self,driver):
    #     self.driver = driver
    #
    # #登录
    # def login(self,username,password):
    #     #输入用户名
    #     #输入密码
    #     #点击登录
    #     # name_text='//input[@id="username"]'
    #     # pwd_txt='//input[@id="password"]'
    #     # login_but='//button[@class="login-btn login-btn1"]'
    #     WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LoginPageLcator.name_text))
    #     self.driver.find_element(*LoginPageLcator.name_text).send_keys(username)
    #     self.driver.find_element(*LoginPageLcator.pwd_txt).send_keys(password)
    #     self.driver.find_element(*LoginPageLcator.login_but).click()
    #
    # #获取登录失败的错误提示信息 -- alert弹窗
    # def get_errorMsg_from_alert(self):
    #     WebDriverWait(self.driver,20).until(EC.alert_is_present())
    #     return self.driver.switch_to.alert.text

    #登录
    def login(self,username,password):
        #输入用户名
        #输入密码
        #点击登录
        # name_text='//input[@id="username"]'
        # pwd_txt='//input[@id="password"]'
        # login_but='//button[@class="login-btn login-btn1"]'
        doc="登录页面_登录功能"
        self.wait_eleVisible(LoginPageLcator.name_text,doc=doc)
        self.input_text(LoginPageLcator.name_text,username,doc)
        self.input_text(LoginPageLcator.pwd_txt,password,doc)
        self.click_element(LoginPageLcator.login_but,doc)
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LoginPageLcator.name_text))
        # self.driver.find_element(*LoginPageLcator.name_text).send_keys(username)
        # self.driver.find_element(*LoginPageLcator.pwd_txt).send_keys(password)
        # self.driver.find_element(*LoginPageLcator.login_but).click()

    #获取登录失败的错误提示信息 -- alert弹窗
    def get_errorMsg_from_alert(self):
        WebDriverWait(self.driver,20).until(EC.alert_is_present())
        return self.driver.switch_to.alert.text
