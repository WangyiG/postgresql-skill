# 在数据库中创建一个叫peewee_test的database
create database peewee_test

import peewee
from peewee import *

# 创建数据库的实例
db = PostgresqlDatabase('peewee_test', user='postgres', password='postgres',host='127.0.0.1') 

# 创建一个指定数据库的基本模型类
class Notes(Model):
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    deleted_at = DateTimeField(index=True, null=True)
    name = CharField()
    data = CharField()
    
    # 设置表名，数据库等
    class Meta:
        table_name = 'notes'
        database = db
     
    
# 创建notes表
if not db.table_exists('notes'):
    db.create_tables([Notes])
    
# 增
## 创建实例后save
Notes(name='peewee3', data='try to create data from peewee3').save()

## 模型类的create方法
Notes.create(name='peewee2', data='try to create data from peewee again3')

## 实例insert然后execute,注意参数是字典元素的一维列表
Notes().insert([
        {'name': 'peewee2', 'data': 'insert data#0 '},
        # 下面两种等效
        {'name': 'peewee2', Notes.data: 'insert data#1 '},
        {Notes.name: 'peewee2', 'data': 'insert data#2 '}
        ]).execute()

## 实例insert_many后execute,注意该方法参数为二维列表
Notes().insert_many([
        ['peewee2', 'insert many data '],
        ['peewee2', 'insert many data#1 '],
        ['peewee2', 'insert many data#2 ']],
        fields=(Notes.name, 'data')).execute()

# 删
## 删除全部数据,谨慎使用,仅删除数据不删除表
Notes.delete().execute()

## 使用where方法有选择的删除数据
Notes.delete().where(Notes.name=='peewee4').execute()

# 改
## 把name为1的行的name修改为peewee4
Notes.update(name='peewee4').where(Notes.name == '1').execute()


# 主键错误的回滚处理
import peewee
try:
    Notes().insert({'id': 164, 'name': '1', 'data': 'it will not rollback of id 11'}).execute()
    Notes().insert({'id': 164, 'name': '2', 'data': 'it will rollback of id 11 #1'}).execute()
except peewee.IntegrityError:
    # 报错了记得回滚
    db.rollback()


# 查,在with db.atomic()上下文中写查询，防止预计错误造成事务中止
## 根据主键查询，未指定主键时会自动生成id主键
with db.atomic():
  print(ret := Notes.get_by_id(164), ret.name, ret.data)
  print(ret := Notes[164], ret.name, ret.data)
  
## 根据模型类的select方法查询,支持limit和offset
with db.atomic():
  select = Notes.select()
  print([i.name for i in Notes.select().limit(10)])
  # 一个语法糖：每页5个，第一页；
  print([i.name for i in Notes.select().paginate(page=1, paginate_by=5)])
  

## 可以转dict，tuple，namedtuple，可以接where
print(list(Notes.select().where(Notes.name == 'peewee3').dicts()))

# where选择器
## in_,注意下划线,注意参数以列表形式传递
print([i.name for i in Notes.select().where(Notes.name.in_(['peewee3','peewee4']))])

## between,实际上字段都重载了__getitem__ 方法，所以可以直接传slice对象，更好的方法是下面2种：
print([i.name for i in Notes.select().where(Notes.id.between(1, 3))])
print([i.name for i in Notes.select().where(Notes.id[slice(2, 4)])])
print([i.name for i in Notes.select().where(Notes.id[3:5])])


## 多个条件，用 ~ ＆ | 连接，注意运算符顺序
print([i.name for i in Notes.select().where((Notes.name == 'peewee2') & (Notes.data == 'insert data#2 '))])

## 模糊匹配Like和regexp,还可以写startswith(),endswith()，contains(),如果用 iregexp() 就是大小写不敏感
print([i.name for i in Notes.select().where(Notes.name % '%peewee%')])
print([i.name for i in Notes.select().where(Notes.name.contains('peewee'))])
print([i.name for i in Notes.select().where(Notes.name.regexp('^peewee[23]'))])




