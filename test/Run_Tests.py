# -*- coding: utf-8 -*
import time, sys
sys.path.append("..")
from public.HTMLTestRunner import HTMLTestRunner
from public.Mail import Email
from public.Config import Config
import unittest

# 指定测试用例为当前文件夹下的 case 目录
test_dir = './case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*l_Test.py')

if __name__ == "__main__":
    #执行测试case,生成测试报告
    now = time.strftime("%Y%m%d%H%M%S")
    report = '../report/' + 'Report_'+ now + '.html'
    with open(report, "wb") as rpt:
        # rpt = open(report, 'wb')
        runner = HTMLTestRunner(stream=rpt,title='一卡通测试报告',description='测试详情： ')
        runner.run(discover)
        # rpt.close()
	# 发送测试报告邮件
    # c = Config().get('mail')
    # receiver = c.get('receiver')
    # server = c.get('server')info
    # sender = c.get('sender')
    # password = c.get('password')
    # e = Email(title = 'TFwork测试报告',
    #           message = 'TFwork测试报告，请查收！',
    #           receiver = receiver,
    #           server = server,
    #           sender = sender,
    #           password = password,
    #           path = report
    #           )
    # e.send()