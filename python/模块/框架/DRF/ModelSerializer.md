## 创建演示app
- 创建app1
```sh
// 切换环境
conda activate drfts
// 进入项目文件夹
cd drftsxs
// 新建app
python manage.py startapp app1
```
- 在setting中注册app1
```py
INSTALLED_APPS = [
    'rest_framework',
    'app0',
    'app1.apps.App1Config',   # 或直接app1,2种方式注册都可以 
]
```
## 配置模型
- 数据库之前已配置,不须再处理
```py
# app1下models.py
from django.db import models

class Book_v1(models.Model):
    name = models.CharField(max_length=32, verbose_name='书名')
    price = models.IntegerField()
    author = models.CharField(max_length=5, verbose_name='作者')

    class Meta:
        db_table = 'tb_books_v1'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
```
- 模型迁移
```sh
// 检查项目目录,项目环境
python manage.py makemigrations
python manage.py migrate
```
## 创建序列化器使用模型序列化器
- app1文件夹下新建serializer.py文件
- 绑定模型后不需要再重写create与update方法
```py
from rest_framework import serializers
from .models import Book_v1
from rest_framework.exceptions import ValidationError


class Book_V1_Serializer(serializers.ModelSerializer):
    class Meta:
        # 模型序列化器绑定模型
        model = Book_v1
        # 注册需要序列化的字段,表模型的property属性字段也可以注册
        # fields = '__all__'  指定所有字段都序列化包括id,但不包括property属性字段
        fields = ['id','name','price','author','price_info'] # 该用法id也需要注册才可序列化


    # 在序列化器中新建局部钩子验证validate_字段名指定字段
    def validate_name(self,attrs):
        # attrs是前端传入的数据
        if attrs.startswith('sb'):
            raise ValidationError("书名不能以sb开头")
        else:
            return attrs

    # 在序列化器中新增全局钩子验证
    def validate(self, attrs):
        if attrs.get('name') == attrs.get('author'):
            raise ValidationError('书名不应与作者名相同')
        else:
            return attrs
```
## 配置视图类
```py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book_v1
from .serializer import Book_V1_Serializer


class Book_v1_view(APIView):

    def get(self, request):
        print(type(request._request))
        book_list = Book_v1.objects.all()
        bs = Book_V1_Serializer(book_list, many=True)
        return Response(bs.data)

    def post(self,request):
        bs = Book_V1_Serializer(data=request.data)
        if bs.is_valid():
            bs.save()  # 生成记录
            return Response(bs.data)
        else:
            return Response({'code':101,'msg':'数据校验失败','error':bs.errors})

class Book_v1_pkview(APIView):

    def get(self,request,pk):
        book = Book_v1.objects.filter(pk=pk).first()
        bs = Book_V1_Serializer(book)
        return Response(bs.data)

    def put(self,request,pk):
        book = Book_v1.objects.filter(pk=pk).first()
        # 修改既有instance又有data,单有instance是查询,单有data是新增
        bs = Book_V1_Serializer(instance=book,data=request.data)
        if bs.is_valid():
            bs.save()  # 生成记录
            return Response(bs.data)
        else:
            return Response({'code':102,'msg':'修改失败','error':bs.errors})

    def delete(self,request,pk):
        book = Book_v1.objects.filter(pk=pk).delete()
        # 模型对象删除返回的是一个tuple
        print(book)
        # 删除并不需要做反序列化,但可以做pk校验
        if book[0]>0:
            return Response({'code':100,'msg':'删除成功'})
        else:
            return Response({'code':103,'msg':'数据不存在'})
```
## 配置路由
- 主路由
```py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app0/', include('app0.urls')),
    path('app1/', include('app1.urls')),
]
```
- 子路由
```py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.Book_v1_view.as_view()),
    path('books/<int:pk>/', views.Book_v1_pkview.as_view()),
]
```
## 运行项目,api测试
```sh
// 指定端口,测试链接为http://127.0.0.1:8013/app1/books/
python manage.py runserver 8013
```
