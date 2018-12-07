#coding: utf-8
from locust import HttpLocust, TaskSet, task
import subprocess
import requests,json,re
import os,time,datetime
from requests_toolbelt import MultipartEncoder
# from public.Log import logger


class SpsTasks(TaskSet):

    email = "tfwork@synative.com"
    password = "123456"
    captcha = "1111"
    upload_video = "./data/video_tfwork.mp4"
    upload_boundary = "------WebKitFormBoundaryjFbWswNdpuy1IeKq"
    login_token = ''
    n = 0

    def on_start(self):
        login_url = "/backend/public/index.php/api/login"
        headers = {
            'Content-Type': 'application/json'
            }
        jsonstring = {
                    "email": self.email,
                    "password": self.password,
                    "captcha": self.captcha
                }
        # login_url = 'http://test.editor.synative.cn/backend/public/index.php/api/login'
        # response = requests.request("POST", login_url, headers=headers, json=jsonstring)
        response = self.client.post(login_url, headers=headers, json=jsonstring)
        results = json.loads(response.text)
        self.login_token = results['data']['access_token']

    @task(0)
    def test_h5(self):
        jsonstring = {
                    'like': '',
                    'by': 'desc',
                    'page': 1,
                    'pageSize': 100
                }  
        headers = {
            "Authorization": "Bearer "+self.login_token
        }
        upload_url = "/backend/public/index.php/api/h5_list?v=2"
        self.client.post(upload_url,headers=headers, json=jsonstring)


    @task(1)
    def test_upload_video(self):
        file_type = re.findall(".*data/(.*)_.*",self.upload_video)
        content_type = re.findall(".*tfwork.(.*)",self.upload_video)
        multipart_encoder = MultipartEncoder(
            fields={
                #数组转字符转：str = ''.join(list)
                'type': ''.join(file_type),
                'randstr': 'uploadTime1543562184199',
                'file': (os.path.basename(self.upload_video),open(self.upload_video,'rb'), ''.join(file_type)+'/'+ ''.join(content_type))
                },
            boundary = self.upload_boundary
            )
        headers = {
            "Content-Type": "multipart/form-data;boundary="+self.upload_boundary,
            "Authorization": "Bearer "+self.login_token
        }
        upload_url = "/backend/public/index.php/api/upload"
        starttime = datetime.datetime.now()
        response = self.client.post( upload_url, headers=headers, data=multipart_encoder)
        results = json.loads(response.text)
        video_uuid = results['data']['id']
        """检查转码是否成功，成功则上传文件完成"""
        check_video_fps = "/backend/public/index.php/api/check_video_fps"
        jsonstring = {
                    "id": video_uuid,
                }
        headers_check = {
            "Authorization": "Bearer "+self.login_token
            }
        time.sleep(3)
        while True:
            response_check = self.client.post(check_video_fps, headers=headers_check, json=jsonstring)
            results_check = json.loads(response_check.text)
            try:
                fps_status = results_check['data']['fps_status']
                """fps_status equals 1 is the state of success."""
                if fps_status == 1:
                    endtime = datetime.datetime.now()
                    self.n += 1
                    print("Upload video and fps Success: "+results_check['data']['url'])
                    break
                else:
                    endtime = datetime.datetime.now()
                    self.n += 1
                    print("Upload video and fps Fail: "+video_uuid)
                    break
            except Exception:
                time.sleep(3)
        # logger.info('第%s次上传视频用时：' % str(self.n) + str(endtime-starttime))
        print('第%s次上传视频用时：' % str(self.n) + str(endtime-starttime))

class SpsLocust(HttpLocust):
    host = "http://test.editor.synative.cn"
    task_set = SpsTasks
    min_wait = 1000
    max_wait = 5000

if __name__ == "__main__":

    result = os.popen('netstat -ano | findstr LISTENING | findstr :8089') 
    text = result.read()
    pid= text [-6:-1]
    find_kill= 'taskkill -f -pid %s' % pid
    result = os.popen(find_kill)

    sps_p = subprocess.Popen("locust -f locust_sps.py", shell=True)
    # # sps_p.kill()
