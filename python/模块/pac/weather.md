## 导包
```py
import requests
from bs4 import BeautifulSoup
import pandas as pd
```
## 封装
- 有些网站将内容封装在不同网址中,直接构建网址即可
```py
def f(city='shanghai',days=7):
    url = f'https://www.tianqi.com/{city}/{days}/'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    resp = requests.get(url=url,headers=header,verify=False)
    weather_info_list = BeautifulSoup(resp.text).find('ul',class_='weaul').find_all('li')
    res = []
    for info in weather_info_list:
        weather = {}
        weather['date'] = info.find('span',class_='fl').text
        weather['zh_date'] = info.find('span',class_='fr').text
        weather['type'] = info.find('div',class_='weaul_z').text
        weather['low'],weather['hige'] = map(lambda x:x.text,info.find_all('span',class_=''))
        res.append(weather)
    return pd.DataFrame(res)

f('beijing',10)
```
