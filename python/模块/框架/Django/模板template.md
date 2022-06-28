## 创建templates文件夹用于存放模板
- 在myapp目录下创建templates目录
- 在templates目录下继续创建一个myapp目录再在其下新建index.html
>模板命名空间,Django的视图搜寻路径是按项目配置文件settings.py下INSTALLED_APPS内注册的app的顺序来遍历其下的templates目录
>但不会去搜寻下一层目录,所以在templates目录下新建一个app同名目录来存放渲染文件,不会造成同名视图被滥用的问题

## 编写urls与views中视图函数
1.views.py中使用render优化index函数
- render函数的作用:载入模板，填充上下文，再返回由它生成的 HttpResponse 对象

```py
from django.shortcuts import HttpResponse,render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # 在注册的多个app的templates目录下搜寻myapp/index.html,不管按何顺序,显然只有myapp下的templates目录下才能找到
    return render(request, 'myapp/index.html', context)
    
```
2.检查根路由urls中是否已经include到子路由urls,如果已经include,直接在子路由urls.py中建立path
```py
path('', views.index, name='index'),
```
