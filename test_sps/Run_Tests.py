from httprunner.api import HttpRunner
import sys
sys.path.append("..")
from public.Log import logger

if __name__ == '__main__':
	'''
	resultclass: HtmlTestResult/TextTestResult，默认值为 HtmlTestResult
	failfast: 设置为 True 时，测试在首次遇到错误或失败时会停止运行；默认值为 False
	dot_env_path: 指定加载环境变量文件（.env）的路径，默认值为当前工作目录下的 .env 文件
	stream
	'''
	kwargs = {
    "failfast":False
    # "report_template":"/path/to/custom_report_template"
    }
	runner = HttpRunner(**kwargs)
	'''  
	运行测试集方式
	文件路径    runner.run("docs/data/demo-quickstart-2.yml")
	文件夹路径  runner.run("docs/data/")
	混合情况    runner.run(["docs/data/", "files/demo-quickstart-2.yml"]) 
	'''	
	runner.run("testcases/v1/sps_api.yml")
	# runner.run("testcases/v1/sps_admin_api.yml")
	
	# get result summary
	# summary = runner.summary
	# logger.info(summary)
	
	'''
	generate html report
	runner.gen_html_report(
		dir_level = 1,  默认为None,report为当前目录，1为父级目录
		html_report_name="demo",
		html_report_template="/path/to/custom_report_template"
	)
	=> reports/demo/demo-1532078874.html
	'''
	# runner.gen_html_report()