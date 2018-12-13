# -*- coding: utf-8 -*
import pymysql
from Support import base64decode

"""
MySQL connection 
"""
def connection(host,name,password,database):
	try:
		db = pymysql.connect(host,name,password,database)
		return db
	except:
	    print("Error: connect failed")

"""
MySQL connection 
"""
def close(db):
	try:
		db.close()
	except:
	    print("Error: close failed")

"""
select sql
"""
def select(db,sql):
	cursor = db.cursor()
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		return results
	except:
	    print("Error: unable to fetch data")

"""
insert、updata、delete sql
"""
def updata(db,sql):
	cursor = db.cursor()
	try:
	    cursor.execute(sql)
	    db.commit()
	except:
		db.rollback()

if __name__ == '__main__':
	"""dev connect"""
	# host = "10.200.11.238"
	# name = "root"
	# password = "hackqy@qq.com"
	# database = "ive-new-backend"

	"""test connect"""
	host = "52.83.155.77"
	name = base64decode(b'c3BzX3Fh')
	password = base64decode(b'cGhwQHN5bmF0aXZl')
	# database = "webtrail_test"
	database = "ive-new-test"

	email = 'case19@synative.com'
	updata_sql = "update users set is_examine=1,set_meal_id=4,strart_time='2018-09-05 08:39:38',expiry_time='2019-12-12 08:00:00' where email='%s'" % email
	select_sql = "select * from captcha where email = '%s'" % email
	"""  """
	conn = connection(host,name,password,database)
	res = select(conn,select_sql)
	# res = updata(conn,updata_sql)
	print(res)
	close(conn)
