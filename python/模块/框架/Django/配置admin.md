## 设置admin页面中文界面
在项目配置文件settings.py的MIDDLEWARE选项中新增语言本地化
``` py
MIDDLEWARE = [
    ...
    # admin界面语言本地化
    'django.middleware.locale.LocaleMiddleware',
]
```

## 创建超级管理员
```sh
python3.9 manage.py createsuperuser
// 按提示输入username:mt,email(可不填),passsword:mangti
```
>密码修改：python3.9 manage.py changepassword username,当然也可在后台直接修改


## 将数据库模型注册到admin中
```py
from django.contrib import admin

from .models import Question,Choice

admin.site.register(Question)
admin.site.register(Choice)
```


## 启动项目进入admin后台,使用超级管理员mt,mangti登录
```sh
python3.9 manage.py runserver 8013
```


## 后台美化
1.在admin.py后台管理文件中修改默认header与title
```py
admin.AdminSite.site_header = "MyDemo系统"
admin.AdminSite.site_title = "模型管理"
```

## 表格美化
- admin中自定义表格要显示的列
```py
from django.contrib import admin
from .models import *

admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Publish)

# admin.site.register(Book) 改用装饰器注册
# 继承admin.ModelAdmin改写list_display属性
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # 必须是列表或元组形式,支持property字段(当前在序列化器fields中也注册了property属性)
    list_display = ['name', 'price', 'publish_detail','author_info']
```
- models类中Meta元类设置中文表名
- models类中重写__str__设置中文表主体
```py
from django.db import models

# 创建4个模型,但因为Book的authors字段ManyToMany关联到Author,会自动多创建一个demo_book_authors中间表
class Book(models.Model):
    # 字段参数verbose_name设置中文列名
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)
    authors = models.ManyToManyField(to='Author')

    class Meta:
        verbose_name = '图书表'
        verbose_name_plural = '图书表'

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
```








