import urllib.request
import sys
import ssl
import json


# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=1X1Faobhn64DUgBLEEqRDFQR&client_secret=V7dP7fDlQEC6qkqfgNZSZqx4v0dKeCGG '
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read().decode()
if __name__== '__main__':
    if(content):
        data = json.loads(content)
        access_token = data['access_token']
        print(access_token)
        