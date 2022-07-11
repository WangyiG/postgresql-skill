## 配置setting
- 注册rest_framework与app
- 配置数据库
- 配置本地化
- 注释中间件csrf认证

## 创建模型
```py
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=32, verbose_name='书名')
    price = models.IntegerField()
    author = models.CharField(max_length=5, verbose_name='作者')

    class Meta:
        db_table = 'tb_books'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
```
## 创建序列化器
- 在app目录下新建serializer.py
- post请求要重写create方法,put请求要重写update方法,目的是指定模型
```py
from rest_framework import serializers
from .models import  Book

class Bookserializer(serializers.Serializer):
    name = serializers.CharField(max_length=32)
    price = serializers.IntegerField()
    author = serializers.CharField(max_length=5)

    def create(self, validated_data):
        # validated_data为校验后的数据
        # 指定保存到Book模型
        book = Book.objects.create(**validated_data)
        return book
```

## 配置视图类
- 防止请求冲突,pk请求，get1个,put,patch,delete应该再新建一个视图类
```py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializer import Bookserializer


class Bookviewset(APIView):

    def get(self, request):
        book_list = Book.objects.all()
        bs = Bookserializer(book_list, many=True)
        return Response(bs.data)

    def post(self,request):
        bs = Bookserializer(data=request.data)
        # 数据校验顺序,字段规则max_length等,局部钩子,全局钩子
        if bs.is_valid():
            bs.save()    
            return Response(bs.data)
        else:
            return Response({'code':101,'msg':'数据校验失败','error':bs.errors})
```
## 配置路由
- 主路由
```py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app0.urls')),
]
```
- 子路由
- pk请求使用转换器books/<int:pk>
```py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.Bookviewset.as_view()),
]
```



