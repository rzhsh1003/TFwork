# -*- coding: utf-8 -*
import time,os,sys
sys.path.append("../..")
from selenium import webdriver
from public.Config import  Config,DRIVER_PATH, REPORT_PATH,LOG_PATH
from public.Log import logger

# 可根据需要自行扩展
#自定义路径
Chorme_path = Config().get('Chorme_path')
CHROMEDRIVER_PATH = os.path.abspath(str(Chorme_path)+'chromedriver.exe') 
#默认路径
#CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'
SERVICE_LOG_PATH = LOG_PATH + '\phantomjs.log'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie, 'phantomjs': webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH, 'phantomjs': PHANTOMJSDRIVER_PATH}


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):
    def __init__(self, browser_type='firefox'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    def get(self, url, maximize_window=True, implicitly_wait=30):
        if self._type == 'phantomjs':
            #service_log_path设置phantomjs浏览器的默认日志文件路径
            self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type],service_log_path=SERVICE_LOG_PATH)
        else:
            self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)    #隐式等待
        return self

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\Screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    b = Browser(browser_type='chrome').get('http://www.baidu.com', maximize_window=True)
    b.save_screen_shot('Test_baidu')
    time.sleep(3)
    b.quit()
