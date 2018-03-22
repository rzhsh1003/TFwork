# -*- coding: utf-8 -*-
"""
url地址下载img
"""
import requests
from bs4 import BeautifulSoup
from Log import logger
import sys,os
from multiprocessing import Pool
from faker import Factory




def UrlgetImg(url,lab='',value='',img='img',src='src',jpg='jpg',num=1):
	fake = Factory().create()
	res=requests.get(url)
	soup=BeautifulSoup(res.text,'html.parser')
	#find_all图片所在位置html路径
	#img_urls=soup.find_all('div',class_='disp_img1')
	img_urls=soup.find_all(lab,attrs=value)
	if img_urls:
		m = 0
		name = fake.first_name()
		for img_url in img_urls:
			n = 0
			for n in range(num):
				try:
					imgs = img_url.find_all(img)[n][src]
					img_res=requests.get(imgs)
					filepath='../img/UrlgetImg/{0}.{1}'.format(name+str(m),jpg) 
					with open(filepath,'wb') as f: 
						f.write(img_res.content)
					#logger.info('下载{0}图片成功'.format(img))
					n+=1
					m+=1
				except Exception as e:
				    print(e)
	else:
		n = 0
		name = fake.first_name()
		for n in range(num):
			try:
				imgs = soup.find_all(img)[n][src]
				img_res=requests.get(imgs)
				filepath='../img/UrlgetImg/{0}.{1}'.format(name+str(n),jpg) 
				with open(filepath,'wb') as f: 
					f.write(img_res.content)
				#logger.info('下载{0}图片成功'.format(img))
				n+=1
			except Exception as e:
				print(e)

if __name__ == '__main__':
	# url = 'http://www.tuku.cn/bizhi/tuji2715_page1.aspx'
	# lab = 'div'
	# value = {'class':'disp_img1'}
	# UrlgetImg(url,lab=lab,value=value)

	# url = 'http://blog.csdn.net/rzhsh1003/article/details/78116448'
	# UrlgetImg(url,num=3)

	#下载cl图片
	print('Parent process %s.' % os.getpid()) #父进程ID
	p=Pool(1) #创建进程池
	for i in range(2839659,2839660):
		url='http://cl.wevu.pw/htm_data/8/1712/{0}_cl.html'.format(i)
		UrlgetImg(url,img='input',num=10)
	p.close()
	p.join()

	# #多线程下载图片
	# print('Parent process %s.' % os.getpid()) #父进程ID
	# p=Pool(4) #创建进程池
	# for i in range(1,5):
	# 	url = 'http://www.tuku.cn/bizhi/tuji2715_page{0}.aspx'.format(i)
	# 	lab = 'div'
	# 	value = {'class':'disp_img1'}
	# 	UrlgetImg(url,lab=lab,value=value)
	# p.close()
	# p.join()