# -*- coding: utf-8 -*
"""
在这里添加各种自定义的断言，断言失败抛出AssertionError就OK。
"""

def assertHTTPCode(response, code_list=None):
    res_code = response.status_code
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        raise AssertionError('响应code不在列表中！')  # 抛出AssertionError，unittest会自动判别为用例Failure，不是Error

def assert_Equal(expect,real):
	if expect == real:
		return 'success'
	else:
		return 'fail'
		raise AssertionError('fail')

def assert_In(expect,real):
	if expect in real:
		return 'success'
	else:
		return 'fail'
		raise AssertionError('fail')

def assert_NotIn(expect,real):
	if expect not in real:
		return 'success'
	else:
		return 'fail'
		raise AssertionError('fail')	

if __name__ == '__main__':
	print (assert_Equal('dddd','dddd'))
