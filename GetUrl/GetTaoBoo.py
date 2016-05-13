# -*- coding: UTF-8 -*-

import requests
import sys

#res = requests.get('https://world.taobao.com/', verify=False)
res1 = requests.get('https://tw.yahoo.com/')
#print(res.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
# print(text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
# print("網頁編碼 : ", res.encoding)

res1.encoding = 'utf-8'
print(res1.text)