## 创建演示app
- 创建app
```sh
// 切换环境
conda activate drfts
// 进入项目文件夹
cd drftsxs
// 新建app
python manage.py startapp app1
```
- 在setting中注册app
```py
INSTALLED_APPS = [
    'rest_framework',
    'app0',
    'app1.apps.App1Config',   # 或直接app1,2种方式注册都可以 
]
```
