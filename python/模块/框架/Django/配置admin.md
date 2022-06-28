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
from .models import Question
from .models import Choice

admin.site.register(Question)
admin.site.register(Choice)

## 启动项目进入admin后台,使用超级管理员mt,mangti登录
python3.9 manage.py runserver 8013
