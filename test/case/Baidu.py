# -*- coding: utf-8 -*
import time,os,sys
sys.path.append("..")
from page.Baidu_main_page import BaiDuMainPage
from page.Baidu_result_page import BaiDuResultPage
sys.path.append("../..")
import unittest
from public.Config import Config,DATA_PATH,REPORT_PATH
from public.Log import logger
from public.HTMLTestRunner import HTMLTestRunner
from public.File_Reader import ExcelReader


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    def sub_setUp(self):
        #self.driver = BrowserDrivers.Chrome()
        #self.driver.get(self.URL)
        self.page = BaiDuMainPage(browser_type='chrome').get(self.URL, maximize_window=True)

    def sub_tearDown(self):
        self.page.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.search(d['search1'])
                time.sleep(1)
                self.page = BaiDuResultPage(self.page)  # 页面跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.page.save_screen_shot('Test_baidu')
                time.sleep(1)
                self.sub_tearDown()

if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    suite=unittest.makeSuite(TestBaiDu)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, title='TFwork')
        runner.run(suite)
        #runner.run(TestBaiDuHTTP('test_baidu_http'))