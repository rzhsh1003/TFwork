# -*- coding: utf-8 -*
"""
文件读取。YamlReader读取yaml文件，ExcelReader读取excel。
"""
# import yaml
import os,sys,time
from xlutils.copy import copy
from xlrd import open_workbook
from ruamel import yaml
import json

class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
        return self._data

    def updata(self,name,value):
        # 修改yml值
        with open(self.yamlf) as f:
            content = yaml.load(f, Loader=yaml.RoundTripLoader)
            content.update({name: value})
        with open(self.yamlf, 'w') as nf:
            yaml.dump(content, nf, Dumper=yaml.RoundTripDumper)


class JsonReader:
    def __init__(self, Jsonf):
        if os.path.exists(Jsonf):
            self.Jsonf = Jsonf
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取json文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.Jsonf, 'rb') as f:
                self._data =json.load(f)  # load后是个generator，用list组织成列表
        return self._data

    def updata(self,name,value):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        with open(self.Jsonf) as f:
            content = json.load(f)
            content[name] = value
        with open(self.Jsonf, 'w') as nf:
            json.dump(content, nf)

class ExcelReader:
    """
    读取excel文件中的内容。返回list。
    如：
    excel中内容为：
    | A  | B  | C  |
    | A1 | B1 | C1 |
    | A2 | B2 | C2 |

    如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
    [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

    如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
    [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

    可以指定sheet，通过index或者name：
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='BaiDuTest')
    """
    def __init__(self, excel, sheet=0, title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int, str]:
                raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                # 第1列为title,第2列为值，返回字典
                # self._data.append(dict(zip(s.col_values(0) , s.col_values(1))))
                title = s.row_values(0)  # 首行为title
                for col in range(1, s.nrows):
                    # 依次遍历其余行，与首行组成dict，拼到self._data中
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    # 遍历所有行，拼到self._data中
                    print (s.row_values(col))
                    self._data.append(s.row_values(col))
        return self._data

    def write(self,row,column,date,excel_path):
        if not self._data:
            workbook = open_workbook(self.excel)
            wb_new = copy(workbook)
            if type(self.sheet) not in [int]:
                raise SheetTypeError('Please pass in <type int> , not {0}'.format(type(self.sheet)))
            else:
                s_new = wb_new.get_sheet(self.sheet)
            s_new.write(row, column, date)
            wb_new.save(excel_path)


if __name__ == '__main__':
    
    # #读取json方法
    y = '../data/test.json'
    reader = JsonReader(y)
    reader.updata('name','2222')
    print(reader.data)


    # #读取yml方法
    # y = '../config/config.yml'
    # reader = YamlReader(y)
    # reader.updata('abc',1234)
    # print(reader.data)

    # 读取excle方法，以及字典元素遍历
    # e = '../data/baidu.xlsx'
    # reader = ExcelReader(e, title_line=False).data
    # print(reader)
    # print(json.dumps(reader))
    # for d in reader:
    #     print (d)
    #     print(dumps(d, indent=4))
        # print (d['search'],d['search1'])

    # #修改excle方法
    # e = '../data/baidu.xlsx'
    # now = time.strftime("%Y%m%d%H%M%S")
    # report = '../report/' + 'Report_'+ now + '.xls'
    # reader = ExcelReader(e,title_line=True)
    # reader.write(row=3,column=0,date='test',excel_path=report)
    
    # 读取excle，发送get请求
    # import requests,json
    # sys.path.append("..")
    # from public.Log import logger
    # e = '../data/cn.xlsx'
    # reader = ExcelReader(e, title_line=True).data
    # for d in reader:
    #     try:
    #         login_url = d['json']
    #         response = requests.request("get", login_url)
    #         results = json.loads(response.text)
    #         login_Auth = results['materials']['relatedStages']
    #         if login_Auth:
    #             logger.info(login_url)
    #     except Exception as e:
    #         logger.info(login_url+'fail')

