## 导包
```py
import requests
from lxml import etree
import re
import json
```
## 请求主页面
```py
url = 'https://desk.zol.com.cn/pinpai/apple/'
host_ = 'https://desk.zol.com.cn'
resp = requests.get(url)
resp.encoding = 'gbk'
```
## 使用xpath解析出子页面列表
```py
et = etree.HTML(resp.text)
resp.close()
routers = et.xpath('//ul[@class="pic-list2  clearfix"]/li/a/@href')[2:]
# 注意得到的以/开头的router应该直接接在host后,而非接在主页面url后
urls = [host_+_ for _ in routers]
urls
```
## 请求子页面并利用re解析出下载页面列表
- 查看子页面源代码,该例将下载页面信息以json格式埋在了源代码script中
- 下载页面的请求与下载略过,无非文件名切一下或使用uuid自己拼
```py
resp = requests.get(urls[3])
obj = re.compile('var deskPicArr.*?=(?P<page>.*?);',re.S)
demo_str = obj.search(resp.text).group('page')
resp.close()
demo = json.loads(demo_str)
target = [item['imgsrc'].replace('##SIZE##',item['oriSize']) for item in demo['list']]
target
```

