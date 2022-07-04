## 导包
```py
import requests
import arrow
```

## 登录页面
- url请不要相信导航栏，而是去请求地址中去找
- get传参用parmas,post传参用data
```py
url = 'https://yun.zt.net.cn/admin/api/custUser/auth'
parma = {
    'username':'13401559204',
    'password':'mangti68',
    'deviceNo':'',
    'platform':''
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
```
## 会话
- 创建一个会话,方便持续爬取
```py
session = requests.Session()
login_page = session.get(url=url,headers=header,params=parma)
login_page.json()
```
## 子页面
- token在上面会话的响应中
- 会话的cookie去请求头中找
- 更新新的headers
```py
main_url = 'https://yun.zt.net.cn/admin/api/millsheet/list'
main_head = header
main_head['_Drame_Authorization'] = login_page.json()['data']['token']
main_head['cookie'] = 'SESSION=ZWRmM2Q4ZWEtODVlZS00ZWMzLTk3Y2QtNWEwNjI4MzM1ZGIy; Hm_lvt_a37e5037a16e3fea4541a57b3f0fa980=1656727484,1656895774; Hm_lpvt_a37e5037a16e3fea4541a57b3f0fa980=1656900155'
main_prama = {
    'page': 1,
    'limit': 10,
    'condition':'', 
    'millsheetNo':'', 
    'specmark':'8', 
    'productnamech':'', 
    'updateTime':'', 
    'displistNo':'', 
}
```
## 爬取新的页面
```py
main_page = session.get(url=main_url,headers=main_head,params=main_prama)
res = main_page.json()
```
## 跳转页面
- 一些链接跳转页面需要重新确定url,重新确定parma
```py
new_url = 'https://yun.zt.net.cn/admin/api/accessLog/addCustDownMillsheet'
new_prama = {
    'millNo': res['data'][0]['millsheetno'],
    'time': int(arrow.now().timestamp())
}
t = session.get(url=new_url,headers=main_head,params=new_prama)
t.json()
```
