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
        fields = ['name', 'price', 'publish', 'authors', 'publish_detail', 'authors_detail']
        # depth = 1 第一层关联的表的关联字段所在行的所有字段都显示,不适合定制该行那些字段显示那些字段不显示
        extra_kwargs = {
            'publish': {'write_only': True},
            'authors': {'write_only': True}
        }

    # publish与authors都是id而非具体信息,定制具体信息字段并注册到fields中
    # 也可以去表模型中@property定制并注册到fields中,这里直接在序列化器中定制 
    
    publish_detail = serializers.SerializerMethodField()
    authors_detail = serializers.SerializerMethodField()

    def get_publish_detail(self,obj):
        return {'name': obj.publish.name, 'city': obj.publish.city,'email':obj.publish.email}
    
    # 使用静态方法定义,不管如何定义,都是通过getattr反射找get_定制字段名
    @staticmethod
    def get_authors_detail(obj):
        author_list = []
        # ManyToMany这里使用all来解构
        for author in obj.authors.all():
            author_list.append({'name': author.name, 'addr': author.author_detail.addr})

        return author_list


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
## 配置视图类
> 关于post新增publish与authors应该传递id值{'publish':1,'authors':[1,2]},因为前端是通过下拉菜单填入,而下拉菜单选项绑定的值应为id
```py
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response


class BookView(APIView):

    def get(self, request):
        book_list = Book.objects.all()
        # 切记queryset对象应当指定many=True
        ser = BookSerializer(instance=book_list, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = BookSerializer(data=request.data)
        if ser.is_valid():
            # 如果校验通过,保存反序列化结果并返回信息
            ser.save()
            return Response({'code': 100, 'msg': '新增成功', 'data': ser.data})
        return Response({'code': 101, 'msg': '校验失败,新增失败', 'err': ser.errors})


class BookDetailView(APIView):

    def get(self, request, pk):
        book = Book.objects.filter(pk=pk).first()
        ser = BookSerializer(instance=book)
        return Response(ser.data)

    def put(self, request, pk):
        book = Book.objects.filter(pk=pk).first()
        # 查询有instance,many 新增有data,修改既有instance(指定要操作那一条对象)也有data(前端获取的数据)
        ser = BookSerializer(instance=book, data=request.data)
        if ser.is_valid():
            # 如果校验通过,保存反序列化结果并返回信息
            ser.save()
            return Response({'code': 100, 'msg': '修改成功', 'data': ser.data})
        return Response({'code': 101, 'msg': '校验失败,修改失败', 'err': ser.errors})

    def delete(self, request, pk):
        Book.object.filter(pk=pk).delete()
        return Response({'code': 100, 'msg': '删除成功'})
```
## 配置路由
```py
# 主路由
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('demo.urls'))
]

# 子路由
from django.urls import path
from .views import BookView,BookDetailView

urlpatterns = [
    path('books/', BookView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
]
```
## 启动项目
```sh
python manage.py runserver
```
## API测试
```sh
# 接口地址
http://127.0.0.1:8000/demo/books/
```

