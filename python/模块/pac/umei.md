## 导入相关库
```py
import requests
from bs4 import BeautifulSoup
import time
```
## 获取图片超链接地址列表
- 编码问题,指定response.encoding
- 指定bs解析的格式为html.parser
- main_page是BeautifulSoup的实例
- find与find_all指定标签与属性,calss与id等py关键字可做下划线处理也可写做attrs={'class':'pic-box'}
- 获取标签内相应属性值用get方法

```py
url = 'https://www.umei.cc/meinvtupian/meinvxiezhen/'
resp = requests.get(url)
resp.encoding = 'utf-8'
main_page = BeautifulSoup(resp.text, 'html.parser')
sub_urls = list(map(lambda x: x.get('data-src'), main_page.find("div", class_="pic-box").find_all('img')))
print(len(sub_urls))
```
## 下载图片
- 获取标签作用的文本用text
- 对于图片等内容用response.content
```py
# 获取图片name列表
# list(map(lambda x:x.text,main_page.find("div", class_="pic-box").find_all('span')))

for i, sub_url in enumerate(sub_urls):
    sub_resp = requests.get(sub_url)
    img_name = sub_url.split('/')[-1]
    with open('img/' + img_name, mode='wb') as f:
        f.write(sub_resp.content)
    print(i)
    time.sleep(2)
print('over')
```

## 关于滚动加载
- 确定滚动加载之后的url
```py
import requests
from bs4 import BeautifulSoup

url = 'https://www.umei.cc/e/action/get_img_a.php'
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
data = {
        'next': '1',
        'table':'news',
        'action': 'getmorenews',
        'limit': '10',
        'small_length': '120',
        'classid': '48'
    }

def f(n):
    data['limit'] = n 
    resp = requests.post(url=url,headers=header,data=data)
    info = BeautifulSoup(resp.text,'lxml')
    res = dict(zip(map(lambda x:x.text,info.find_all('span')),map(lambda x:x.get('src'),info.find_all('img'))))
    return res   

f(15)
```

## 异步
- 准备一个辅助文件funchelp.py
```py
import requests
from bs4 import BeautifulSoup
from aiohttp import request
import asyncio

url = 'https://www.umei.cc/e/action/get_img_a.php'
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
data = {
        'next': '1',
        'table':'news',
        'action': 'getmorenews',
        'limit': '10',
        'small_length': '120',
        'classid': '25'
    }

def get_urls1():
    data['limit'] = '150'
    resp = requests.post(url=url,headers=header,data=data)
    resp.close()
    info = BeautifulSoup(resp.text,'lxml')
    urls = list(map(lambda x:x.get('src'),info.find_all('img')))
    return urls

async def get(url):
    async with request("GET", url) as response:
        return await response.content.read()
```
- 异步爬取
```py
from aiomultiprocess import Pool 
import asyncio
import aiofiles
from aiohttp import request
from funchelp import get,get_urls
import uuid

async def main():
    urls = get_urls()
    async with Pool() as pool:
        async for result in pool.map(get, urls):
            async with aiofiles.open('img/timg/'+str(uuid.uuid4())+'.jpg',mode='wb') as f:
                await f.write(result)

await main()
```
