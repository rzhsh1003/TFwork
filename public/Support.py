# -*- coding: utf-8 -*
"""一些支持方法，比如加密"""
import hashlib
import sys
import base64
from Log import logger


class EncryptError(Exception):
    pass


def sign(sign_dict, private_key='', encrypt_way='MD5'):
    """传入待签名的字典，返回签名后字符串
    1.字典排序
    2.拼接，用&连接，最后拼接上私钥
    3.MD5加密"""
    dict_keys = list(sign_dict.keys())
    dict_keys.sort()
    string = ''
    for key in dict_keys:
        if sign_dict[key] is None:
            pass
        else:
            string += '{0}={1}&'.format(key, sign_dict[key])
    string = string[0:len(string) - 1]
    string = string.replace(' ', '')
    return encrypt(string, salt=private_key, encrypt_way=encrypt_way)


def encrypt(string, salt='', encrypt_way='MD5'):
    """根据输入的string与加密方法，按照encrypt方式进行加密，并返回加密后的字符串"""
    string += salt
    if encrypt_way.upper() == 'MD5':
        hash_string = hashlib.md5()
    elif encrypt_way.upper() == 'SHA1':
        hash_string = hashlib.sha1()
    else:
        logger.exception(EncryptError('请输入正确的加密方式，目前仅支持 MD5 或 SHA1'))
        return False

    hash_string.update(string.encode())
    return hash_string.hexdigest()

def base64encode(string):
    encode_string = base64.b64encode(string)
    return encode_string

def base64decode(string):
    decode_string = base64.b64decode(string)
    return decode_string

if __name__ == '__main__':
    print(encrypt('age=19&name=uncle',encrypt_way='MD5'))

    dict_test = {'name':'uncle','age':19}
    print(sign(dict_test,encrypt_way='MD5'))

    # name = base64encode(b'sps_qa')
    # pw = base64encode(b'php@synative')
    # print(name,pw)