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
