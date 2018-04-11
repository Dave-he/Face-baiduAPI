# coding:utf-8
import base64
import urllib
import urllib.parse
import urllib.request
import sys
import cv2
import numpy
import json
'''
人脸探测
'''

# 二进制方式打开图片文件
f = open('../2.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"face_fields":"age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities","image":img,"max_face_num":5}
params = urllib.parse.urlencode(params).encode(encoding='UTF-8')

request_url = "https://aip.baidubce.com/rest/2.0/face/v1/detect"
access_token = '24.f74582487bf452901fdffa1289f085f4.2592000.1522850809.282335-10883437'
request_url = request_url + "?access_token=" + access_token
request_url.encode('UTF-8')
requested = urllib.request.Request(url=request_url, data=params)
requested.add_header('Content-Type', 'application/x-www-form-urlencoded')
requested.coding='UTF-8'
response = urllib.request.urlopen(requested)
content = response.read().decode()
if content:
    #print(content)
    data=json.loads(content)
    facerect=data['result'][0]['location']
    left=facerect['left']
    top=facerect['top']
    width=facerect['width']
    height=facerect['height']
    srcimage = cv2.imread('../2.jpg',1)
    cv2.rectangle(srcimage,
                (left,top),(left+width,top+height),
                (255,255,0),1)	   
    cv2.imshow('image',srcimage)

cv2.waitKey(0)


