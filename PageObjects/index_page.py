# @Time :2021-10-13 11:27
# @Author :ShaylorLaw
# @File :index_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class IndexPage:

    def __init__(self,driver):
        self.driver=driver

    def isExist_Index_ele(self):
        #等待10秒，元素有没有出现 //a[text()='首页']
        #如果存在就返回True，如果不存在，就返回False
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//a[text()='首页']")))
            return True
        except:
            return False