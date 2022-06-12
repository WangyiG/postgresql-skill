# 文件如record_0.txt,内部内容格式为{name:xx,timestamp:xxx,content:xxx},{name:xx,timestamp:xxx,content:xxx}

# 1.以jsonb的格式整个存入
import orjson
from peewee import PostgresqlDatabase,Model,TextField

# 这里指定peewee传入的字符串是postgres中的jsonb类型，peewee_test数据库需要手动在postgres中创建:create database peewee_test

db = PostgresqlDatabase('peewee_test', user='mt', password='postgres',host='127.0.0.1',field_types={'json':'jsonb'}) 

# 自定义一个JSONField字段类,指定field_type,并在db中指定数据库中该type如何解析
class JSONField(TextField):
    field_type = 'json'
    def db_value(self, value):
        return value

    def python_value(self, value):
        if value is not None:
            return orjson.loads(value)
          
class BaseModel(Model):
    class Meta:
        database = db

class Notes(BaseModel):
    json_data = JSONField()
    
# 创建notes表
db.create_tables([Notes])

# 读取txt文件,提取字段存入列表,以便后续批量插入
import pathlib as pl
path = pl.Path('/Users/mt/Documents/python/群友题解/IO数据/records/record_0.txt')
with path.open('r',encoding='utf-8') as fr:
    data_list = []
    for i in fr:
        data_list.append([i.strip()])
data_list[0]

Notes().insert_many(data_list,fields = [Notes.json_data]).execute()


# 2.以name，timestamp，content字段存入表格
import orjson
from peewee import PostgresqlDatabase,Model

db = PostgresqlDatabase('peewee_test', user='mt', password='postgres',host='127.0.0.1') 

class BaseModel(Model):
    class Meta:
        database = db

class AnotherNotes(BaseModel):
    name = CharField()
    timestamp = TimestampField()
    content = TextField()   

# 处理文件，存入列表
import pathlib as pl
path = pl.Path('/Users/mt/Documents/python/群友题解/IO数据/records/record_0.txt')
with path.open('r',encoding='utf-8') as fr:
    data_list = []
    for i in fr:
        data_list.append(orjson.loads(i))
data_list[0]

# 批量插入
AnotherNotes().insert_many(data_list).execute()


# 3.使用扩展,扩展不必自己创建jsonfield
from playhouse.postgres_ext import *
db = PostgresqlExtDatabase('peewee_test', user='mt', password='postgres',host='127.0.0.1') 
class BaseModel(Model):
    class Meta:
        database = db

class Record2(BaseModel):
    json_data = BinaryJSONField(index=True,index_type='GIN')
    
db.create_tables([Record2])

import pathlib as pl
import orjson
path = pl.Path('/Users/mt/Documents/python/群友题解/IO数据/records/record_2.txt')
with path.open('r',encoding='utf-8') as fr:
    data_list = []
    for i in fr:
        data_list.append([orjson.loads(i)])
data_list[0]

with db.atomic():
    Record2().insert_many(data_list,fields = [Record2.json_data]).execute()



# 总结：
‘’‘
新建字段类，根据field_type,指定数据库以jsonb格式解析
对于insert_many，2次data_list的区别：
第一个data_list是一个二维列表,列表元素为:"{xxx:xxx,xx:xx}"字符串,只包含数据内容，需要指定fields参数，注意该参数是个列表形式，fields=[x,xx]
第二个data_list是一个一维列表，列表元素为:{'name':xx,'timestamp':xx,'content':xx},一一对应了field name，timestamp，content及其数据内容
在postgre中查找那么包含张三:SELECT * FROM record2 WHERE json_data @>'{"name":"张三"}'
’‘’



