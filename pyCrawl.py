# -*- coding:UTF-8 -*-
# import sys
import requests
# reload(sys)

# sys.setdefaultencoding('uft-8')
resp=requests.get('http://news.sina.com.cn/')
resp.encoding = 'utf-8'
htmlcontend =resp.text

print type(htmlcontend)
with open('news.html','w') as html:
    html.writelines(htmlcontend.encode('utf-8'))
