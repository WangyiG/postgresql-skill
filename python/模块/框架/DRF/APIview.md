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
    
    # 在模型中封装一个property属性
    @property
    def price_info(self):
        return [{'this book price':f'这本书的价格是{self.price}美元'},{'this book name':f'书名为{self.name}'}]
    
    

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
    # 自增的id可以做序列化,指定read_only不做反序列化
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=32)
    price = serializers.IntegerField()
    author = serializers.CharField(max_length=5)
    
    # 新增自定义方法字段及其对应显示,函数名为get_自定义方法字段
    # 可用于跨表展示外键信息
    new_price = serializers.SerializerMethodField(read_only=True)
    def get_new_price(self,obj):
        # obj是在view中序列化之后的模型对象即当前案例中的book
        return f'new_price is ${obj.price}'
        
    # 也可以对model中的property属性,进行序列化
    price_info = serializers.ListField(read_only=True)
        
        
    # 重写create与update方法
    def create(self, validated_data):
        # validated_data为校验后的数据
        # 指定保存到Book模型
        book = Book.objects.create(**validated_data)
        return book
        
    def update(self, instance,validated_data):
        # instance是要修改的对象,validated_data为校验后的数据
        # 这里instance为什么指定到了Book模型,因为视图类put函数中instance指定的book是Book模型的序列化
        instance.name = validated_data.get('name')
        instance.price = validated_data.get('price')
        instance.author = validated_data.get('author')
        # 模型对象自带的save
        instance.save()
        return instance
        
        
    # 在序列化类中新建局部钩子验证:validate_字段名,指定字段
    def validate_name(self,attrs):
        # attrs是前端传入的数据
        if attrs.startswith('sb'):
            raise ValidationError("name不能以sb开头")
        else:
            return attrs

    # 在序列化器类中新增全局钩子验证:validate
    def validate(self, attrs):
        if attrs.get('name') == attrs.get('author'):
            raise ValidationError('书名不应与作者名相同')
        else:
            return attrs
           
```

## 配置视图类
- drf都是使用视图类,APIview是**drf**中最顶层的视图类,继承自django的view
- 只要继承了APIview,无论中间件是否注释,csrf认证都无效了
- 防止请求冲突,pk请求，get单个,put,patch,delete应该再新建一个视图类
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
            
            
class Bookpkview(APIView):

    def get(self,request,pk):
        book = Book.objects.filter(pk=pk).first()
        bs = Bookserializer(book)
        return Response(bs.data)

    def put(self,request,pk):
        book = Book.objects.filter(pk=pk).first()
        # 修改既有instance又有data,单有instance是查询,单有data是新增
        bs = Bookserializer(instance=book,data=request.data)
        if bs.is_valid():
            bs.save()  # 生成记录
            return Response(bs.data)
        else:
            return Response({'code':102,'msg':'修改失败','error':bs.errors})

    def delete(self,request,pk):
        book = Book.objects.filter(pk=pk).delete()
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
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app0.urls')),
]
```
- 子路由
- pk请求使用转换器books/<int:pk>
- 使用as_view传递视图函数地址
```py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.Bookview.as_view()),
    path('books/<int:pk>/', views.Bookpkview.as_view()),
]
```

## 运行项目
```sh
python manage.py runserver 8013
```

