# -*- coding: utf-8 -*-
"""
#url参数生成字典
"""
def UrlgetDict(url,args1='?',args2='&',args3='=',num=1):
	#拆分得到参数信息，如：['a=1', 'b=2', 'c=3']
	url_list = (url.split(args1)[num]).split(args2)
	url_dict = {}
	for i in url_list:
		#遍历分别把参数信息加入字典i
		value = i.split(args3)
		url_dict.update(dict(zip(value[0],value[1])))
	return url_dict

if __name__ == '__main__':
	url = "http://www.baidu.com?a=1&b=2&c=3"
	url_dict = UrlgetDict(url)
	print (url_dict)