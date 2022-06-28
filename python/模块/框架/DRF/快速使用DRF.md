## DFM安装
```sh
sudo conda create -n drf python=3.8 django==3.2.4 djangorestframework psycopg2
```

## 创建dfmdemo项目
```sh
/Users/mt/miniforge3/envs/drf/bin/django-admin startproject drfdemo
```
虚拟环境最好还是使用pycharm,进入preferences-python interpreter-show all 选择conda环境，找刚刚安装的drf


## 注册DFM
在settings.py配置文中新增配置项
```py
INSTALLED_APPS = [
     ...,
    'rest_framework',
]
...

## 创建APP
切换到项目目录,注意检查是否是drf环境,两种app创建方式
```sh
python manage.py startapp stuapp  // 用于drf
django-admin startapp students // 原生django使用
```

## 注册APP
在项目配置文件settings.py文件中,两种注册方式
```py
INSTALLED_APPS = [
     ...,
    'rest_framework',
    'stuapp',
    'students.apps.StudentsConfig',
]
...


## 创建模型
配置数据库
```sql



