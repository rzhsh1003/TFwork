# -*- coding: utf-8 -*
import time,os,sys
sys.path.append("..")
from page.Selenium_page import SeleniumPage
sys.path.append("../..")
import unittest
from public.Config import Config,DATA_PATH
from public.Log import logger
from public.File_Reader import ExcelReader
from public.Assertion import assert_Equal
from selenium.webdriver.common.by import By


class Login(unittest.TestCase):

    ''' sps_ui '''
    def sub_setUp(self):
        #self.driver = BrowserDrivers.Chrome()
        #self.driver.get(self.URL)`
        URL = Config().get('IVE_URL')
        self.page = SeleniumPage(browser_type='chrome').get(URL, maximize_window=True)
        self.page.Login('case5@synative.com','123456','1234')
        self.page.wait(1)
        self.page.save_screen_shot('test_login_sussess')

    def sub_tearDown(self):
        self.page.quit()

    # def test_login_sussess(self):
    #     ''' Login Sussess '''
    #     self.sub_setUp()
    #     # self.page.F5
    #     # self.page.implicitly_wait(30)
    #     self.page.Login('case@synative.com','123456','1234')
    #     self.page.implicitly_wait(30)
    #     rest = assert_Equal('http://test.editor.synative.cn/#/index',self.page.current_url)
    #     logger.info('test_login_sussess:'+rest)
    #     self.page.save_screen_shot('test_login_sussess')
    #     self.sub_tearDown()
    
    # def test_login_fail(self):
    #     ''' The user password is mistaken! '''
    #     self.sub_setUp()
    #     self.page.Login('case@synative.com','123456','1234')
    #     self.page.implicitly_wait(3)
    #     res = self.page.find_element(By.XPATH, "/html/body/div[2]/p").text
    #     rest = assert_Equal('The user password is mistaken!',res)
    #     logger.info('test_login_fail1:'+rest)
    #     self.sub_tearDown()

    def test_new_project(self):
        ''' New Project '''
        self.sub_setUp()
        # self.page.F5
        # self.page.implicitly_wait(30)
        self.page.Add_project('python-test')
        self.page.implicitly_wait(30)
        rest = assert_Equal('http://test.editor.synative.cn/#/index',self.page.current_url)
        logger.info('test_new_project success:'+rest)
        self.page.wait()
        self.page.save_screen_shot('new_project_success')
        self.sub_tearDown()


        
