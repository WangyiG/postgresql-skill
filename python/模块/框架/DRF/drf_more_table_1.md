## 在drf环境下创建项目与app并配置项目
1. 数据库中新建drf_more_table数据库
```sql
create database drf_more_table
```
2. 新建项目与app
```sh
django-admin startproject drf_more_table
cd drf_more_table
python manage.py startapp demo 
```
3. 配置setting.py
```py
# 注册rest_framework与app
INSTALLED_APPS = [
          ...
    'rest_framework',
    'demo',
]

# 配置数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'drf_more_table',
        'USER': 'mt',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
      }
}

# 修改本地化
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False

```

## 配置表模型并迁移激活
```py
from django.db import models

# 创建4个模型,但因为Book的authors字段ManyToMany关联到Author,会自动多创建一个demo_book_authors中间表
class Book(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)
    authors = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.name

    @property
    def publish_detail(self):
        return {'id':self.publish.id,'name':self.publish.name,'email':self.publish.email}

    @property
    def author_info(self):
        author_list = []
        for author in self.authors.all():
            author_list.append({'name':author.name,'birthday':author.author_detail.birthday,'addr':author.author_detail.addr})
        return author_list

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # OneToOne是ForeignKey的一种特殊情况unique一定是True
    author_detail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)

class AuthorDetail(models.Model):
    telephone = models.BigIntegerField()
    birthday = models.DateField()
    addr = models.TextField()

class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

```
```sh
python manage.py makemigrations
python manage.py migrate
```
## 配置序列化器
```py
from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','name','price','publish','authors','publish_detail','author_info']
        extra_kwargs = {
            'publish':{'write_only':True},
            'authors':{'write_only':True}
        }

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorDetail
        fields = '__all__'

class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = '__all__'
```
## 扩展,多表写入
- 有一个问题author表与author_detail表数据库中分离,但用户不知道,新增author时应当一次提交author表字段与author_detail表字段
- 重写反序列化字段并重写create与update方法
```py
class AuthorSerializer(serializers.ModelSerializer):
          class Meta:
                    model = Author
                    # 重点在于telephone与addr不是author表字段而是author_detail表字段
                    fields = ['name','age','telephone','addr']
          telephone = serializers.BigIntegerField(write_onle = True)
          addr = serializers.CharField(write_onle = True)
          # 为了一次提交分别存2个表
          def create(self,validated_data):
                    # 注意有先后顺序
                    detail = AuthorDetail.objects.create(telephone = validated_data.get('telephone'),addr = validated_data.get('addr'))
                    author = Author.objects.create(author_detail = detail,name = validated_data.get('name'),age = validated_data.get('age'))
                    return author
```

## 配置视图类
```py
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *


class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewset(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailViewset(ModelViewSet):
    queryset = AuthorDetail.objects.all()
    serializer_class = AuthorDetailSerializer


class PublishViewset(ModelViewSet):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer
```
## 配置路由
```py
# 主路由
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('demo.urls'))
]

# 子路由
from rest_framework import routers
from django.urls import path,include
from . import views

router = routers.SimpleRouter()
router.register('books',views.BookViewset,basename='books')
router.register('author',views.AuthorViewset,basename='author')
router.register('publish',views.PublishViewset,basename='publish')
router.register('author_detail',views.AuthorDetailViewset,basename='author_detail')

urlpatterns = [
    path('',include(router.urls))
]

```
## 启动项目
```sh
python manage.py runserver
```
## API测试
```sh
# 接口地址一堆类似如下
http://127.0.0.1:8000/api/books/
```
