## 在postgre中新建一个djdemo数据库
```sql
create database djdemo
```

## 配置postgre数据库
>Django中使用postgre的第一项准备是安装psycopg2模块,mac下我之前已安装:conda install psycopg2

>修改配置为本地时区,在项目配置文件settings.py中修改TIME_ZONE = 'Asia/Shanghai',USE_TZ = False

1.在项目配置文件settings.py的DATABASES选项下修改配置
先将默认的sqlite3数据库配置注释掉
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',     # 指定postgres引擎
        'NAME': 'djdemo',                              # 数据库名,Django不会帮你创建,需要自己进入数据库创建
        'USER': 'mt',                                  # 默认用户名
        'PASSWORD': 'postgres',                        # 数据库密码
        'HOST': '127.0.0.1',
        'PORT': '5432',
      }
    }
```

2.在数据库管理文件model.py下新建2个模型
- question包括描述和发布时间字段
- choice包括选项和当前得票数,并且使用外键约束来限制每个选项属于那个问题
- 给模型增加 __str__() 方法,增强模型在命令行与Django自带的admin后台的可读性

```py
from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # Django 会在外键字段名后追加字符串 "_id",所以这里实际字段是question_id
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)    
    
    def __str__(self):
        return self.choice_text
```

3.激活模型
- makemigrations 为模型的改变生成迁移文件
- migrate 执行迁移
```sh
python3.9 manage.py makemigrations
python3.9 manage.py migrate
```

4.数据库迁移被分解成生成和应用两个命令是为了能够在代码控制系统上提交迁移数据并使其能在多个应用里使用
```sh
// 进入交互式 Python 命令行
python3.9 manage.py shell

// 简单尝试orm操作api,交互式命令行,所以以下逐行执行
from polls.models import Choice, Question
Question.objects.all()
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id,q.question_text,q.pub_date
q.question_text = "What's up?"
q.save()
Question.objects.filter(question_text__startswith='What')
from django.utils import timezone
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)
Question.objects.get(pk=1)
q = Question.objects.get(pk=1)
q.was_published_recently()
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)
c.question
c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()
```



## ORM操作模型表以及其中的数据
>orm操作后应当重新激活模型来进行生效
1.对已有数据的模型新增字段时需要注意数据对齐的问题,2种解决方法：
- 字段中指定default=xxx
- 或允许空值,指定null=True,blank=True

2.在models.py中使用模型对象.object实例来调用模型方法
2.1 增
```py
Question.object.create(question_text='吃西瓜会长胖吗?')
```


























