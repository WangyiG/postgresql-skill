## tip
- 开发者工具中Elements是实时html与页面html源文件不同
- 以梨视频为例,视频的真实地址在Elements中但不在源文件
- Network中找到的请求地址返回的响应中的地址与真实地址也存在差异

## Referer
- 网络来路
- 利用检查页面的网络来路Referer是否正确来阻止或允许访问

## 导包
```py
import requests
from jsonpath import jsonpath
```

## 请求准备
```py
# Elements中真实目标地址
target_url = 'https://video.pearvideo.com/mp4/third/20220630/cont-1766669-10411777-200721-hd.mp4'
# 导航地址
root_url = 'https://www.pearvideo.com/video_1766669'
# 请求地址
main_url = 'https://www.pearvideo.com/videoStatus.jsp?contId=1766669&mrd=0.8743587203521135'
# 为处理真实地址与响应地址差异做准备
contId = 'cont-'+root_url.split('_')[-1]

# 配置Referer
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Apple\
                   WebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Referer': root_url
}
```

## 请求并下载
```py
resp = requests.get(url=main_url,headers=header)
data = resp.json()
resp.close()

# 单个文件直接用左边,批量处理用右边
target_url == jsonpath(data,'$..srcUrl')[0].replace(jsonpath(data,'$.systemTime')[0],contId)

# 下载
with open(f'vidio/{contId}.mp4',mode='wb') as f:
    f.write(requests.get(target_url).content)
```
