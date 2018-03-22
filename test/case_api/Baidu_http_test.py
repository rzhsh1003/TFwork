# -*- coding: utf-8 -*
import unittest, sys
sys.path.append("../..")
from public.Config import Config, REPORT_PATH
from public.Client import HTTPClient
from public.Log import logger
from public.HTMLTestRunner import HTMLTestRunner
from public.Assertion import assertHTTPCode,assert_Equal
import requests,json


class TestBaiDuHTTP(unittest.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='GET')

    def test_baidu_http(self):
        res = self.client.send()
        logger.debug(res.text)
        assertHTTPCode(res, [200])
        self.assertIn('百度一下，你就知道', res.text)

''' 接口测试'''
class test_get_event_list(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/sec_get_event_list/"
        self.querystring = {"eid":"1"}
        self.headers = {
            'Authorization': "Basic cmVuemhhbnNoZW5nOm5ld2NhcGVjLjA=",
            'Cache-Control': "no-cache",
            'Postman-Token': "2814aa51-fd96-417a-bc76-5a95194fae94"
            }
        self.response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        self.results = json.loads(self.response.text)

    def test_get_event_list(self):
        assert_Equal(self.response.status_code, 200)

    def test_get_event_list2(self):
        assert_Equal(self.results['message'], 'success')

    def test_get_event_list3(self):
        assert_Equal(self.results['data']['eid'], 1)



if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    suite=unittest.makeSuite(test_get_event_list)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='接口html报告')
        runner.run(suite)
        #runner.run(TestBaiDuHTTP('test_baidu_http'))