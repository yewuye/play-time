# -*- coding: UTF-8 -*-
import time
import base64
import string
import random
import hashlib
import urllib
import urllib2


# 获取sign签名
def getReqSign(parser, appkey):
    uri_str = ''
    for key in sorted(parser.keys()):
        if key == 'app_key':
            continue
        uri_str += "%s=%s&" % (key, urllib.quote(str(parser[key]), safe=''))
    sign_str = uri_str + 'app_key=' + appkey

    hash_md5 = hashlib.md5(sign_str)
    return hash_md5.hexdigest().upper()


url = 'https://api.ai.qq.com/fcgi-bin/ptu/ptu_facemerge'
# 获取当前时间戳
t = time.time()
# 读取图片，转换为base64编码
with open("/home/qianran/下载/qian.jpg", "rb") as imageFile:
    pixel = base64.b64encode(imageFile.read())  # 已确保无空格
# 产生随机字符串
salt = ''.join(random.sample(string.ascii_letters + string.digits, 10))
# 包装成一个字典
params = {
    'app_id': 1106886350,     # 应用标识(AppId)
    'time_stamp': int(t),     # 请求时间戳（秒级）
    'nonce_str': salt,  # 随机字符串
    'model': 6,  # 变妆编码
    'image': pixel,  # 待处理图片
}
appkey = '6goE9jsZtOS6Ka0n'
params.update({'sign': getReqSign(params, appkey)})
# -------------以上准备请求参数-------------------
data = urllib.urlencode(params)
# data = data.encode('utf-8')
new_url = urllib2.Request(url=url, data=data)
response = urllib2.urlopen(new_url).read()
res = eval(response)['data']['image']

fh = open("new.jpg", "wb")
fh.write(base64.b64decode(res))
fh.close()
