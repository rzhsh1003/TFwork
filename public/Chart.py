# -*- coding: utf-8 -*
import matplotlib.pyplot as plt 
import time,sys
import numpy as np
sys.path.append("..")
from public.Config import Config

"""
2-D Chart Line 
"""
def chart_line(x1,y1,label='Frist line',xlabel='Date',ylabel='Response Time(ms)',title='Sps performance test index'):
	today= time.strftime('%Y-%m-%d',time.localtime(time.time()))
	plt.plot(x1,y1,label=label,linewidth=1,color='r',marker='o', markerfacecolor='blue',markersize=5) 
	# plt.plot(x2,y2,label='second line') 
	plt.xlabel(xlabel+'(%s)' %today) 
	plt.ylabel(ylabel) 
	plt.title(title) 
	plt.legend() 
	plt.show() 

"""
2-D Chart Round
"""
def chart_round(labels,sizes,colors,explode):  
	plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)    
	plt.axis('equal')    
	plt.show() 

if __name__ == '__main__':
	# x1=range(0,10) 
	# x2=range(0,10) 
	# y1=[10,13,5,40,30,60,70,12,55,25] 
	# y2=[5,8,0,30,20,40,50,10,40,15]
	# chart_line(x1,y1)

	# labels='frogs','hogs','dogs','logs'    
	# sizes=15,20,45,10    
	# colors='yellowgreen','gold','lightskyblue','lightcoral'    
	# explode=0,0.1,0,0  
	# chart_round(labels,sizes,colors,explode)

	''' Export data generated 2-D Chart Line'''
	# yml_path = '../test_sps/data/sps.yml'
	# x1 = Config(yml_path).get('export_time_list')
	# y1 = Config(yml_path).get('export_usetime_list')
	# num = Config(yml_path).get('export_num')
	# average =int(np.sum(y1)/num)
	# chart_line(x1,y1,label='export average(ms):%s' %average)

	''' Upload data generated 2-D Chart Line'''
	yml_path = '../test_sps/data/sps.yml'
	x1 = Config(yml_path).get('upload_time_list')
	y1 = Config(yml_path).get('upload_usetime_list')
	num = Config(yml_path).get('upload_num')
	average =int(np.sum(y1)/num)
	chart_line(x1,y1,label='upload average(ms):%s' %average)