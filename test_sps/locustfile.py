#coding: utf-8
from locust import HttpLocust, TaskSet, task
from httprunner.task import LocustTask
import debugtalk
import subprocess,os

class WebPageTasks(TaskSet):
    def on_start(self):
        self.test_runner = LocustTask(self.locust.file_path, self.client)

    @task
    def test_specified_scenario(self):
        self.test_runner.run()

class WebPageUser(HttpLocust):
    host = "http://test.editor.synative.cn"
    task_set = WebPageTasks
    min_wait = 1000
    max_wait = 5000
    file_path = "testcases/v1/sps_api_locust.yml"

if __name__ == "__main__":

    result = os.popen('netstat -ano | findstr LISTENING | findstr :8089') 
    text = result.read()
    pid= text [-6:-1]
    find_kill= 'taskkill -f -pid %s' % pid
    result = os.popen(find_kill)

    sps_p = subprocess.Popen("locusts -f locustfile.py", shell=True)
    # sps_p.kill()