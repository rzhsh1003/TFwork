# import logging
# import random

# import zmq
# from httprunner.exceptions import MyBaseError, MyBaseFailure
# from httprunner.api import prepare_locust_tests
# from httprunner.runner import Runner
# from locust import HttpLocust, TaskSet, task
# from locust.events import request_failure

# logging.getLogger().setLevel(logging.CRITICAL)
# logging.getLogger('locust.main').setLevel(logging.INFO)
# logging.getLogger('locust.runners').setLevel(logging.INFO)


# class WebPageTasks(TaskSet):
#     def on_start(self):
#         self.test_runner = Runner(self.locust.config, self.locust.functions, self.client)

#     @task
#     def test_any(self):
#         test_dict = random.choice(self.locust.tests)
#         try:
#             self.test_runner.run_test(test_dict)
#         except (AssertionError, MyBaseError, MyBaseFailure) as ex:
#             request_failure.fire(
#                 request_type=self.test_runner.exception_request_type,
#                 name=self.test_runner.exception_name,
#                 response_time=0,
#                 exception=ex
#             )


# class WebPageUser(HttpLocust):
#     task_set = WebPageTasks
#     min_wait = 10
#     max_wait = 30

#     file_path = "testcases/v2/sps_api.yml"
#     locust_tests = prepare_locust_tests(file_path)
#     functions = locust_tests["functions"]
#     tests = locust_tests["tests"]
#     config = {}
#     host = config.get('base_url', '')

import subprocess,os
if __name__ == "__main__":

    result = os.popen('netstat -ano | findstr LISTENING | findstr :8089') 
    text = result.read()
    pid= text [-6:-1]
    find_kill= 'taskkill -f -pid %s' % pid
    result = os.popen(find_kill)

    sps_p = subprocess.Popen("locusts -f testcases/v2/sps_api_locust.yml", shell=True)
    # # sps_p.kill()
