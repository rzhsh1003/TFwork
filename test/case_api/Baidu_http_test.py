# -*- coding: utf-8 -*
import unittest, sys
sys.path.append("../..")
from public.Config import Config, REPORT_PATH
from public.Client import HTTPClient
from public.Log import logger
from public.HTMLTestRunner import HTMLTestRunner
from public.Assertion import assertHTTPCode,assert_Equal
import requests,json
import http.cookiejar


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


''' IVE Login '''
class test_login(unittest.TestCase):
    def setUp(self):
        self.r = requests.session()
        self.url = "http://test.editor.synative.com/backend/public/index.php/api/login"
        self.querystring = {
                    "email": "317975868@qq.com",
                    "password": "111111",
                    "captcha": "1111"
                }
        self.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
            }
        self.response = self.r.post(self.url, headers=self.headers, params=self.querystring)
        self.results = json.loads(self.response.text)
        logger.info(self.results['data']['access_token'])

    # def test_login(self):
    #     assert_Equal(self.response.status_code, 200)
    #     assert_Equal(self.results['message'], 'success')

    def test_account_refresh(self):
        self.refresh_url = "http://test.editor.synative.com/backend/public/index.php/api/account_refresh"
        self.headers1 = {
                "Authorization": "Bearer "+self.results['data']['access_token']
            }
        self.response1 = self.r.post(self.refresh_url, headers=self.headers1)
        self.results1 = json.loads(self.response1.text)
        assert_Equal(self.results1['message'], 'success')



if __name__ == '__main__':
    report = REPORT_PATH + '\\report1.html'
    suite=unittest.makeSuite(test_login)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='TFwork', description='接口html报告')
        runner.run(suite)
        #runner.run(TestBaiDuHTTP('test_baidu_http'))