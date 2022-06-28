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
```


## 创建模型
1.配置数据库

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',     
        'NAME': 'drf',                              
        'USER': 'mt',                                  
        'PASSWORD': 'postgres',                        
        'HOST': '127.0.0.1',
        'PORT': '5432',
      }
    }
```
2.配置模型
```py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name='姓名')
    sex = models.BooleanField(default=1, verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')
    classmate = models.CharField(max_length=10, verbose_name='班级编号')
    description = models.TextField(max_length=1000, verbose_name='个性签名')

    class Meta:
        db_table = 'tb_student'
        verbose_name = '学生'
        verbose_name_plural = verbose_name
        
```
3.激活模型
```sh
python manage.py makemigrations
python manage.py migrate
```

## 配置urls与views
1.使用drf需要先创建一个序列化器,在stuapp目录下创建序列化器serializers.py文件
```py
from rest_framework import serializers
from .models import Student

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # 指定字段序列化
        # fields = ['id','name','age']

```

2.stuapp这里使用drf,进入stuapp应用下的views.py
```py
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentModelSerializer

class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

```

3.使用drf子路由urls.py的配置也要走rest_framework
```py
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('stu',views.StudentModelViewSet,basename='stu')

urlpatterns = [

              ]+router.urls

```

4.配置项目总路由urls.py
```py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('stuapp.urls'))
]

```

## 启动项目
```sh
python manage.py runserver 8013
```
回到浏览器打开:http://127.0.0.1:8013/api/stu/


## 解决跨域
1.在项目目录下安装django-cors-headers
```py
pip install django-cors-headers
```
2.在settings文件中注册corsheaders
```py
INSTALLED_APPS = [
     ...,
    'rest_framework',
    'stuapp',
    'students.apps.StudentsConfig',
    'corsheaders',
]
```
3.在settings文件中间件中注册
```py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',

     ...
    ]
```
4.setting文件最后新增3句code
```py
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = ('*')
```





