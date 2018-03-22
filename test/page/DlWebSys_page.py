# -*- coding: utf-8 -*
import time,datetime, sys
sys.path.append("..")
from selenium.webdriver.common.by import By
from common.Page import Page
sys.path.append("../..")
from public.Log import logger


class DlWebSysPage(Page):
    
    def Login(self, organbm,usercode,passwd):
        """登录功能"""
        self.organbm= (By.ID, 'organbm')
        self.usercode = (By.ID, 'usercode')
        self.passwd = (By.ID, 'passwd')
        self.login_button = (By.XPATH, ".//*[@id='loginform']/button")

        self.find_element(*self.organbm).send_keys(organbm)
        self.find_element(*self.usercode).send_keys(usercode)
        self.find_element(*self.passwd).send_keys(passwd)
        self.find_element(*self.login_button).click()
                        
    def Kwgl_Page(self):
        """卡务管理""" 
        self.kwgl = (By.XPATH, ".//*[@id='dock']/div/a[1]/img")
        self.find_element(*self.kwgl).click()

    def addmoney(self,tranamt):
        """现金存款"""
        self.xjck = (By.XPATH, ".//*[@id='accordion1']/div[2]/table/tbody/tr[3]/td")
        self.tranamt = (By.ID, 'tranamt')
        self.amtchk = (By.ID, 'amtchk')

        self.find_element(*self.xjck).click()
        self.switch_to_frame('97')
        self.find_element(*self.tranamt).send_keys(tranamt)
        self.find_element(*self.amtchk).click()

        
    def foradd(self):
        """循环加款"""
        self.dk = (By.XPATH, ".//*[@id='form1']/div/table/tbody/tr[1]/td[3]/a/img")
        self.savemoney = (By.XPATH, ".//*[@id='savemoney']")
        self.qd = (By.XPATH, "html/body/div[3]/table/tbody/tr[2]/td[2]/div/div[3]/div/div[1]/div[3]")
        
        self.find_element(*self.dk).click()
        self.wait(1)
        self.implicitly_wait(30)
        self.find_element(*self.savemoney).click()
        starttime = time.strftime('%H:%M:%S',time.localtime(time.time()))
        self.implicitly_wait(30)
        self.wait(2)
        self.find_element(*self.qd).click()
        endtime = time.strftime('%H:%M:%S',time.localtime(time.time()))
        start=datetime.datetime.strptime(starttime,"%H:%M:%S")
        end=datetime.datetime.strptime(endtime,"%H:%M:%S")
        ut = end-start
        return ut

        

    def Htgl_Page(self):
        """后台管理""" 
        self.Htgl = (By.XPATH, ".//*[@id='dock']/div/a[4]/img")
        self.find_element(*self.Htgl).click()

    def Addbm(self,departid):
        """增加同级部门""" 
        self.bmgl = (By.XPATH, ".//*[@id='accordion1']/div[2]/table/tbody/tr[7]/td/table/tbody/tr/td[3]")
        self.addParent = (By.ID, 'addParent')
        self.departid = (By.ID, 'departid')
        self.addbm = (By.XPATH, ".//*[@id='lays']/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input")

        self.find_element(*self.bmgl).click()
        self.switch_to_frame('31')
        self.find_element(*self.addParent).click()
        self.find_element(*self.departid).send_keys(departid)
        self.find_element(*self.addbm).click()

    def deletebm(self):
        """删除部门""" 
        self.treeDemo = (By.ID, 'treeDemo_6_ico')
        self.remove = (By.ID, 'remove')

        self.find_element(*self.treeDemo).click()
        self.find_element(*self.remove).click()
        # self.switch_to_alert()
        # logger.info(self.switch_to_alert().text)

    def Addzhlx(self,acctypename):
        """新增账户类型""" 
        self.sjzd = (By.XPATH, ".//*[@id='accordion1']/div[3]/div[3]")
        self.zhlx = (By.XPATH, ".//*[@id='accordion1']/div[4]/table/tbody/tr[9]/td/table/tbody/tr/td[3]")
        self.addzhlx = (By.XPATH, ".//*[@id='toptoolbar']/div[1]/div[1]/span")
        self.acctypename = (By.ID, 'acctypename')
        self.addzh = (By.XPATH, ".//*[@id='container']/table/tbody/tr/td[2]/input")

        self.find_element(*self.sjzd).click()
        self.wait(0.3)
        self.find_element(*self.zhlx).click()
        self.switch_to_frame('61')
        self.find_element(*self.addzhlx).click()
        self.switch_to_frame(0)
        self.find_element(*self.acctypename).send_keys(acctypename)
        self.find_element(*self.addzh).click()
        self.switch_to_parent_frame()


    def Kaihu(self,username,departname,idserial):
        """开户""" 
        self.kaihu = (By.XPATH, ".//*[@id='accordion1']/div[2]/table/tbody/tr[1]/td/table/tbody/tr/td[3]")
        self.duka = (By.XPATH, ".//*[@id='openleft']/table[1]/tbody/tr[1]/td[3]/a/img")
        self.username = (By.ID, 'username')
        self.departname = (By.ID, 'departname')
        self.seidserial = (By.ID, 'idserial')
        self.openAcc = (By.ID, 'idserial')

        self.find_element(*self.kaihu).click()
        self.implicitly_wait(3)
        self.find_element(*self.duka).click()
        self.implicitly_wait(3)
        self.find_element(*self.username).send_keys(username)
        self.find_element(*self.departname).send_keys(departname)
        self.find_element(*self.idserial).send_keys(idserial)
        self.find_element(*self.openAcc).click()
        