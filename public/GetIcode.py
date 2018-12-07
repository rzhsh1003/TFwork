from urllib import request

def GetIcode(pic_link,save_path):
	try:
	    request.urlretrieve(pic_link, save_path)
	except:
	    pass

if __name__ == '__main__':
	i=1
	pic_link = 'http://192.168.102.226/eCard-t5/Images.aspx'
	for i in range(1,3):
		save_path = '../img/ecard/{0}.jpg'.format(i)
		GetIcode(pic_link,save_path)
		i+=1
