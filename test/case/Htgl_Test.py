# -*- coding: utf-8 -*
import time,os,sys
sys.path.append("..")
from page.DlWebSys_page import DlWebSysPage
sys.path.append("../..")
import unittest
from public.Config import Config,DATA_PATH
from public.Log import logger
from public.File_Reader import ExcelReader
from public.Assertion import *
from selenium.webdriver.common.by import By


class Htgl(unittest.TestCase):
    ''' 后台管理 '''
    URL = Config().get('URL')
    page = DlWebSysPage(browser_type='firefox').get('http://192.168.112.118:8088/DlWebSys/', maximize_window=True)
    page.Login('00000001','0004','111111')

    def sub_setUp(self):
        '''
        delete sys_department where DEPTNAME='TFwork部门';
        delete sys_acctype where ACCTYPENAME='TFwork账户类型';
        '''
        self.page.Kwgl_Page()

    def sub_tearDown(self):
        self.page.quit()


    def test_case1(self):
        ''' 循环现金存款 ''' 
        self.sub_setUp()
        self.page.addmoney('5000')
        x=1
        while x < 61:  
            try:
                tt = self.page.foradd()
                logger.info('第'+str(x)+'次'+'加款用时：'+str(tt))
            except Exception as e:
                logger.error('加款失败：'+str(e))
            x+=1
        self.sub_tearDown()
        

    # def test_case1(self):
    #     ''' 增加同级部门 ''' 
    #     self.sub_setUp()
    #     self.bm = 'TFwork部门'
    #     self.page.Addbm(self.bm)
    #     self.page.implicitly_wait(3)
    #     res = self.page.find_element(By.XPATH, ".//*[@id='treeDemo']").text
    #     rest = assert_In(self.bm,res)
    #     logger.info('test_addbm:'+rest)
    #     #self.page.save_screen_shot('test_addbm')
        
    # def test_case2(self):
    #     ''' 删除部门 ''' 
    #     self.page.deletebm()
    #     self.page.implicitly_wait(3)
    #     res = self.page.switch_to_alert().text
    #     logger.info(res)
    #     rest = assert_Equal('删除成功',res)
    #     logger.info('test_deletebm:'+rest)
    #     #self.page.save_screen_shot('test_deletebm')
    #     self.sub_tearDown()
        
    # def test_case3(self):
    #     ''' 新增账户类型 '''
    #     self.zhlx = 'TFwork账户类型' 
    #     self.page.Addzhlx(self.zhlx)
    #     self.page.implicitly_wait(3)
    #     res = self.page.find_element(By.XPATH, "html/body/div[3]/table/tbody/tr[2]/td[2]/div/div[2]").text
    #     rest = assert_Equal('添加成功',res)
    #     logger.info('test_addzhlx:'+rest)
    #     self.page.implicitly_wait(3)
    #     self.page.save_screen_shot('test_addzhlx')
    #     self.page.refresh
    #     self.sub_tearDown()
