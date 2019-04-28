# -*- coding: utf-8 -*
from pymediainfo import MediaInfo
import json

def GetMediaInfo(file):
	media_info = MediaInfo.parse(file)
	data = media_info.to_json()
	return data

if __name__ == '__main__':

    # ToBase64("./desk.jpg",'desk_base64.txt')  # 文件转换为base64
    res = json.loads(GetMediaInfo('../data/1.mp4')) # base64编码转换为二进制文件
    print ('比特率：'+str(((res['tracks'])[1])['bit_rate']))
    print ('采样率：'+str(((res['tracks'])[1])['samples_count']))
