# -*- coding: utf-8 -*
import time,sys
sys.path.append("..")
from common.Browser import Browser
sys.path.append("../..")
from public.Log import logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Page(Browser):
    def __init__(self, page=None, browser_type='firefox'):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)

    @property
    def current_window(self):
        return self.driver.current_window_handle

    #@property装饰器就是负责把一个方法变成属性调用：self.title
    @property  
    def title(self):
        return self.driver.title

    #获取当前url
    @property
    def current_url(self):
        return self.driver.current_url

    #页面后退
    @property
    def back(self):
        return self.driver.back()

    #页面前进
    @property
    def forward(self):
        return self.driver.forward()

    #页面刷新
    @property
    def refresh(self):
        return self.driver.refresh() 

    #键盘Enter
    @property
    def Enter(self):
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform();   

    def get_driver(self):
        return self.driver

    def wait(self, seconds=3):
        time.sleep(seconds)

    def implicitly_wait(self, seconds=10):
        return self.driver.implicitly_wait(seconds)

    def execute(self, js, *args):
        self.driver.execute_script(js, *args)

    def move_to(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)

    def switch_to_window(self, partial_url='', partial_title=''):
        """切换窗口
            如果窗口数<3,不需要传入参数，切换到当前窗口外的窗口；
            如果窗口数>=3，则需要传入参数来确定要跳转到哪个窗口
        """
        all_windows = self.driver.window_handles
        if len(all_windows) == 1:
            logger.warning('只有1个window!')
        elif len(all_windows) == 2:
            other_window = all_windows[1 - all_windows.index(self.current_window)]
            self.driver.switch_to.window(other_window)
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if partial_url in self.driver.current_url or partial_title in self.driver.title:
                    break
        logger.debug(self.driver.current_url, self.driver.title)


    def switch_to_frame(self, param):
        self.driver.switch_to.frame(param)

    #返回到父frame,如果当前已是主文档,则无效果
    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    #从frame中切回主文档
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def accept(self):
        return self.driver.accept()

if __name__ == '__main__':
    from selenium.webdriver.common.by import By
    b = Page(browser_type='chrome').get('http://www.baidu.com', maximize_window=True)
    b.find_element(By.ID, 'kw').send_keys('AAAA')
    b.Enter
    time.sleep(3)
    #b.save_screen_shot('Test_baidu')
    b.refresh
    time.sleep(3)
    b.quit()
