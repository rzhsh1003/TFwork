import random
import requests,json
import sys,re
import os,time,datetime
from requests_toolbelt import MultipartEncoder
sys.path.append("..")
from public.Log import logger
from public.Config import Config
from public.Chart import chart_line

Test_env = "online"
Sps_test_url = "http://test.editor.synative.cn"
# Sps_test_url = "http://dev.editor.synative.com"
Sps_admin_url = "http://test.ve-admin.synative.cn"
S3_cn = "http://s3.cn-northwest-1.amazonaws.com.cn/nx-synative-ve"
email = "tfwork@synative.com"
password = "123456"
# email = "liuquanyang@altamob.com"
# password = "qweqwe123"
captcha = "1111"
upload_image = "./data/image_tfwork.png"
# upload_video = "./data/image_tfwork.png"
upload_video = "./data/video_tfwork.mp4"
upload_boundary = "------WebKitFormBoundaryjFbWswNdpuy1IeKq"

""" 
skip this test in online environment
"""
def skip_test_in_online_env():
    return Test_env == "online"

""" 
Log information 
"""
def logger_info(msg):
    logger.info(msg)

""" 
For login to return to user auth 
"""
def login(email,password,captcha):
    login_url = Sps_test_url+"/backend/public/index.php/api/login"
    jsonstring = {
                "email": email,
                "password": password,
                "captcha": captcha
            }
    response = requests.request("POST", login_url, json=jsonstring)
    results = json.loads(response.text)
    login_token = results['data']['access_token']
    return login_token

""" 
For locust to return to user auth ，Please note when not in use.
"""
login_token = login(email,password,captcha)


""" 
Get form-data request data
"""
def upload_file(filepath):
    # file_name = os.path.basename(filePath)
    file_type = re.findall(".*data/(.*)_.*",filepath)
    content_type = re.findall(".*tfwork.(.*)",filepath)
    multipart_encoder = MultipartEncoder(
        fields={
            #数组转字符转：str = ''.join(list)
            'type': ''.join(file_type),
            'randstr': 'uploadTime1543562184199',
            'file': (os.path.basename(filepath),open(filepath,'rb'), ''.join(file_type)+'/'+ ''.join(content_type))
            },
        boundary = upload_boundary
        )
    return multipart_encoder

""" 
Get form-data request data
"""
def update_file(filepath,app_id,rid,timepos):
    # file_name = os.path.basename(filePath)
    file_type = re.findall(".*data/(.*)_.*",filepath)
    content_type = re.findall(".*tfwork.(.*)",filepath)
    multipart_encoder = MultipartEncoder(
        fields={
            #数组转字符转：str = ''.join(list)
            'app_id': str(app_id),
            'rid': rid,
            'timepos': str(timepos),
            'type': ''.join(file_type),
            'file': (os.path.basename(filepath),open(filepath,'rb'), ''.join(file_type)+'/'+ ''.join(content_type))
            },
        boundary = upload_boundary
        )
    return multipart_encoder


""" 
Check the successful state of exported zip 
"""
def check_zip(id,channel,access_token):
    starttime = time.time()
    check_zip_url = Sps_test_url+"/backend/public/index.php/api/check_zip"
    jsonstring = {
                "id": id,
                "channel": channel,
            }
    headers = {
            "Authorization": "Bearer "+access_token
        }
    time.sleep(5)
    yml_path = './data/sps.yml'
    n = Config(yml_path).get('export_num')
    dulist = Config(yml_path).get('export_usetime_list')
    dtlist = Config(yml_path).get('export_time_list')
    while True:
        response = requests.request("POST", check_zip_url, headers=headers, json=jsonstring)
        results = json.loads(response.text)
        try:
            status = results['data']['task_status']
            endtime = time.time()
            usetime = int((endtime-starttime)*1000)
            n += 1
            """Status equals 2 is the state of success."""
            if status == 2:
                zipurl = results['data']['zip_url']
                down_url = S3_cn + '/' + zipurl
                name = zipurl.split('/')[4]
                z = requests.get(down_url) 
                with open('download/'+name, "wb") as code:
                    code.write(z.content)
                """ 统计下载使用时间，记录日志和数据"""
                logger.info('第%s次导出成功，用时：%sms' % (str(n) ,str(usetime)))
                logger.info("Export zip url: "+down_url)
                break
            elif status == 3:
                logger.info('第%s次导出成功，用时：%sms' % (str(n) ,str(usetime)))
                logger.info("Export zip url fail: "+jsonstring['id']+jsonstring['channel'])
                break
            else:
                time.sleep(5)
        except:
            time.sleep(5)
    dulist.append(usetime)
    dtlist.append(time.strftime('%H:%M:%S',time.localtime(starttime)))
    Config(yml_path).updata('export_usetime_list',dulist)
    Config(yml_path).updata('export_time_list',dtlist)
    Config(yml_path).updata('export_num',n)    
    return status

""" 
Check the successful state of upload video fps
"""
def check_video_fps(id,access_token):
    starttime = time.time()
    check_video_fps = Sps_test_url+"/backend/public/index.php/api/check_video_fps"
    jsonstring = {
                "id": id,
            }
    headers = {
            "Authorization": "Bearer "+access_token
        }
    time.sleep(5)
    yml_path = './data/sps.yml'
    n = Config(yml_path).get('upload_num')
    uulist = Config(yml_path).get('upload_usetime_list')
    utlist = Config(yml_path).get('upload_time_list')
    while True:
        response = requests.request("POST", check_video_fps, headers=headers, json=jsonstring)
        results = json.loads(response.text)
        try:
            fps_status = results['data']['fps_status']
            """fps_status equals 1 is the state of success."""
            endtime = time.time()
            usetime = int((endtime-starttime)*1000)
            n += 1
            if fps_status == 1:
                logger.info('第%s次上传视频成功，用时：%sms' % (str(n) ,str(usetime)))
                logger.info("Upload url: "+S3_cn + '/' +results['data']['url'])
                break
            else:
                logger.info('第%s次上传视频失败，用时：%sms' % (str(n) ,str(usetime)))
                logger.info("Upload video and fps Fail: "+id)
                break
        except:
            time.sleep(5)
    uulist.append(usetime)
    utlist.append(time.strftime('%H:%M:%S',time.localtime(starttime)))
    Config(yml_path).updata('upload_usetime_list',uulist)
    Config(yml_path).updata('upload_time_list',utlist)
    Config(yml_path).updata('upload_num',n)
    return fps_status

if __name__ == '__main__':
    # x = 0
    # while x < 30:
    #     x += 1
    #     id ='01A1C52F-DCD6-A847-DEE2-7A7882914F92'
    #     check_video_fps(id,login_token)

    # id =3791
    # check_zip(id,'default',login_token)

    import numpy as np
    yml_path = './data/sps.yml'
    x1 = Config(yml_path).get('upload_time_list')
    y1 = Config(yml_path).get('upload_usetime_list')
    num = Config(yml_path).get('upload_num')
    average =int(np.sum(y1)/num)
    chart_line(x1,y1,label='upload average(ms): %s' %average)
