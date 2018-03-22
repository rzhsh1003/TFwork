1. 安装python，版本为python3 
      1）下载安装包。 在python官方网站选择下载python3版本的安装包
         下载地址：https://www.python.org/downloads/。  
      2）安装完之后，需要在系统的环境变量path中加入D:\Python3;D:\Python3\Scripts (D:\Python3是python刚安装好的目录）
      3）验证python是否安装成功。打开cmd, 然后可以在命令行输入 python --version
      4）验证pip, 在cmd里执行以下命令：pip.

2. 安装selenium.
     1) cmd执行命令：pip install selenium==2.53.1        
     2) 验证是否安装成功。输入以下命令：pip show selenium
     3）chromedriver地址：http://chromedriver.storage.googleapis.com/index.html
        IEDriverServer地址：http://selenium-release.storage.googleapis.com/index.html
     注：Firefox支持版本46.0.1
         IE设置：http://blog.csdn.net/zyl26/article/details/51011073

3. 安装PyYaml（PY解析YAML语言）
     1) cmd执行命令：pip install PyYaml
     注：PyYaml地址：

4. 安装xlrd（excel读）
     1) cmd执行命令：pip install xlrd 
     注：xlrd地址：https://github.com/python-excel/xlrd

5. 安装xlwt（excel写）
     1) cmd执行命令：pip install xlwt 
     注：xlrd地址：https://github.com/python-excel/xlwt

6.安装JMESPath（解析JSON）
     1) cmd执行命令：pip install JMESPath 
     注：JMESPath地址：

7. 安装Faker（构造数据）
     1) cmd执行命令：pip install Faker
     注：Faker地址：

8. phantomjs关闭问题
     提示：PermissionError:WinError32另一个程序正在使用此文件，进程无法访问。
     解决：修改..\Python36\Lib\site-packages\selenium\webdriver\phantomjs\service.py
     修改前：
          def send_remote_shutdown_command(self):
              if self._cookie_temp_file:
                  os.remove(self._cookie_temp_file)
     修改后：
          def send_remote_shutdown_command(self):
          try:
              if self._cookie_temp_file:
                  os.remove(self._cookie_temp_file)
          except:
              pass

9.安装tesseract(识别图片) 
      地址：http://digi.bib.uni-mannheim.de/tesseract
      设置环境变量： 
      1）将tesseract.exe添加到环境变量PATH中，例如: D:\Tesseract-OCR
      2）将tessdata目录的上级目录所在路径添加至TESSDATA_PREFIX环境变量中，例如: D:\Tesseract-OCR
      注：中文字库地址：http://www.qianduanzaixian.com/detail.do?id=51
          训练字库：jTessBoxEditor

10.安装Pillow、Pytesseract(识别图片)
      1) cmd执行命令：pip install Pillow、Pytesseract
      注：Pillow、Pytesseract地址：

11.爬虫requests、beautifulsoup4
      1) cmd执行命令：pip install requests、beautifulsoup4