## 配置setting
- 注册rest_framework与app
- 配置数据库
- 配置本地化

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
## 模型迁移

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
- drf都是使用视图类,APIview是**drf**中最顶层的视图类,继承自django的view
- 只要继承了APIview,无论中间件是否注释,csrf认证都无效了
- 防止请求冲突,pk请求，get1个,put,patch,delete应该再新建一个视图类
```py
'''
APIview核心函数as_view和dispatch
1.as_view,闭包函数(定义在函数内部,对外部作用域有引用),用于把视图函数地址传递给路由
2.dispatch,通过django的request生成一个新的drf的Request实例对象request传递给视图类,处理全局异常,无论是执行认证,权限,频率校验还是视图执行的异常都将被捕获
3.新request对象最重要的属性request.data(前端传入的数据都能被拿到包括传入json),老的request.POST只接受urlencode和formdata编码传入的数据
4.新request对象method,path属性通过getattr反射老的request.method与request.path,未做变更
APIview执行流程
包装新的Request对象,视图类中请求函数传入的request对象都是新包装的(新增了data属性,反射其它老的request对象属性),对三大校验与视图函数执行做异常捕获
'''

```
```py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializer import Bookserializer


class Bookview(APIView):

    def get(self, request):
        # request._request才是原先django的request
        print(type(request._request))
        book_list = Book.objects.all()
        # 对后端数据进行序列化,多返回值查询应指定many=True,默认为False
        bs = Bookserializer(book_list, many=True)
        return Response(bs.data)

    def post(self,request):
        # 假设前端传入json格式数据,新对象也有POST属性(反射得到)与老对象即request._request的POST属性为空(因为不支持json编码传入的数据)
        # 如果前端传入的是urlencode与formdata,三者都有值
        print(request.POST)          
        print(request._request.POST)
        print(request.data)
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
    path('books/', views.Bookview.as_view()),
]
```

## 运行项目
```sh
python manage.py runserver 8013
```

