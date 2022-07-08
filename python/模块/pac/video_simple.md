## 导包
```py
import requests
from lxml import etree
import re
import json
from glob import glob
```
## 从视频首页获取每集url
```py
url = 'https://www.97dsja.com/v/45652.html'
host_ = 'https://www.97dsja.com'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'   
}
resp = requests.get(url,headers=header,verify=False)
et = etree.HTML(resp.text)
resp.close()
page_urls = [host_+ url  for url in et.xpath('//*[@id="dx2"]/li/a/@href')]
```
## 获取每集的m3u8地址
```py
for i,page_url in enumerate(page_urls,1):
    page_resp = requests.get(page_url,verify=False)
    m3u8_url = re.findall('"url":"(.+)","url_next"',page_resp.text)[0].replace('\\','')
    page_resp.close()
    m3u8_content = requests.get(m3u8_url,verify=False)
    with open('video/zrwh/'+f'zrwh{i}.m3u8',mode='wb') as f:
        f.write(m3u8_content.content)
    m3u8_content.close()
```
## 获取ts_host并下载ts文件
- m3u8文件中ts是相对路径
- 注意m3u8文件中是否有加密，一般加密会有key.key字样
- 在视频网页拖动下视频,开发者工具中找到ts的绝对路径
```py
ts_host = 'https://m3.taopianplay1.com/taopian/54fdb532-e89b-4567-bc07-aa93a0c6a79b/bddfddc\
3-e89a-4db9-a0b1-e3389ab295ab/47787/0ddb96a6-60fd-4ba6-ab4f-542ac8d834ea/SD/'

with open('video/zrwh/zrwh1.m3u8','r',encoding='utf-8') as f:
    n = 0
    for line in f:
        line = line.strip()
        if not line.startswith('#'):
            ts_resp = requests.get(ts_host+line)
            with open('video/zrwh/zrwhts1/'+f'{n}.ts',mode='wb') as tsf:
                tsf.write(ts_resp.content)
            n += 1
            ts_resp.close()
```

## 合并ts文件到视频
- 使用QuickTime Player,编辑:将剪辑添加到结尾,文件:导出为xxx
- 代码写入,按顺序将ts写入mp4(这里quicktime可以打开ts不能打开mp4,腾讯视频打开mp4验证)
```py
# 一定要先将ts排好序
files =sorted(glob('video/zrwh/zrwhts1/*.ts'),key=lambda x:int(x.split('/')[-1][:-3]))
for file in files:
    with open(file,'rb') as fr:
        with open('video/zrwh/zrwhts1/'+'rzwh_video.mp4','ab+') as fw:
            fw.write(fr.read())
```



