# -*- coding: utf-8 -*
import base64

def ToBase64(file, txt):
    with open(file, 'rb') as fileObj:
        file_data = fileObj.read()
        base64_data = base64.b64encode(file_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()

def ToFile(txt, file):
    with open(txt, 'rb') as fileObj:
        base64_data = fileObj.read()
        file_data = base64.b64decode(base64_data)
        fout = open(file, 'wb')
        fout.write(file_data)
        fout.close()

if __name__ == '__main__':

    # ToBase64("./desk.jpg",'desk_base64.txt')  # 文件转换为base64
    ToFile("../data/base64.txt",'../data/base64.mp4')  # base64编码转换为二进制文件