## 安装Django
```sh
pip install diango
```
## 创建项目
切换到项目目录,diango-admin startproject mydemo
```sh
cd /Users/mt/Documents/pyproject/MyDjango

/Users/mt/.local/bin/django-admin startproject mydemo
```

## 熟悉默认项目文件
brew install tree
切换至创建的mydemo目录,执行tree
```
mydemo
├── manage.py               // 项目管理，启动项目，创建app，数据管理，经常使用但很少修改该文件
└── mydemo                  
    ├── __init__.py
    ├── asgi.py             // 异步，接收网络请求
    ├── settings.py         // 项目配置，app注册，数据库配置（常做配置）
    ├── urls.py             // url路径与函数对应关系配置（常做配置）
    └── wsgi.py。           // 同步，接收网络请求
  
```

## APP应用组件的创建
项目中不同的业务逻辑应当使用不同的组件来构建
切换至manage.py所在的mydemo项目目录使用manage.py来创建app应用组件
```sh
python3.9 manage.py startapp myapp
```

## 熟悉APP组件默认文件
```
myapp
├── __init__.py
├── admin.py              // django提供的后台管理
├── apps.py
├── migrations            // 数据库迁移调整时使用
│   └── __init__.py
├── models.py             // 数据库对象操作（重要）
├── tests.py              // 单元测试用
└── views.py              // 函数定义(重要)
```

## 在项目配置settings.py中注册APP
修改INSTALLED_APPS选项,新增myapp.apps.MyappConfig
```py

# 其中myapp指app组件的目录
# apps指apps.py文件
# 再使用MyappConfig注册(注意:这里的Myappconfig的首字母一定要大写)
'myapp.apps.MyappConfig'

```

## 编写urls与views中视图函数的对应关系
打开urls.py文件,先导入views,新增一个url与函数对应
```py

from myapp import views

# path接收参数url与函数
# url一开始使用的admin/index,但跳不开admin的登陆,这也符合常识,admin下的路径理应都需要权限方合理
path('index', views.index),

```

回到views.py文件,新增一个刚刚在urls.py中构建对应关系的函数
```py
from django.shortcuts import render,HttpResponse

def index(request):
    # 必须要有一个request参数,HttpResponse函数需要先导入
    return HttpResponse('页面测试,success!')
    
```

## 启动项目
使用项目管理manage.py来启动项目
- 因为默认的8000端口已经被我的vue占用了,这里指定8013端口来测试下
```sh
python3.9 manage.py runserver 8013
```

## 验证
打开浏览器,进入http://127.0.0.1:8013/index,'页面测试,success!'




















