# 1.Field类用于描述模型属性到数据库列的映射,创建模型类时,字段被定义为类属性
# https://peewee.readthedocs.io/en/latest/peewee/models.html#fields

# 1.1 多种常用的Field类
{
  AutoField():自增整数型,且该属性一定是primary_key=True，事实上，当模型类未设置主键时，会自动实现id = AutoField()，隐式的创建一个id主键
  IntegerField():int,
  CharField():varchar,
  TextField():text,
  UUIDField():uuid,
  DateField():date,可以调用year，month，day属性
  TimeField():time,可以调用hour，minute，second属性
  DateTimeField():datetime,可以调用date和time的所有属性
  ForeignKeyField():外键类型
}

# 1.2 字段初始化参数，即所有字段类型可接受的参数及其默认值
{
  null = False ：是否允许空值，
  index = False ：是否在此列创建索引，
  unique = False ：是否在此列上创建唯一索引，
  column_name = None : 显示指定数据库中的列名,用于解决数据库中列名与关键字冲突，如：create_ = TextField(column_name = 'create'),
  default = None ：用作未初始化模型的默认值，
  primary_key = False :是否为表的主键,
  constraints = None ：一个或多个约束，例如[Check('price > 0')]，
  index_type = None ：指定自定义索引类型，例如，对于Postgres，可以指定或索引类型为'BRIN'或'GIN'
}

# 1.3 特殊字段的特殊参数
{
  CharField ：max_length，
  [DateField,TimeField,DateTimeField] : formats,
  TimestampField : resolution, utc,
  ForeignKeyField : model, field, backref, on_delete, on_update, deferrable lazy_load
}
'''
注意：如果使用的是接受可变类型（list、dict 等）的字段，并且希望提供默认值，则最好将默认值包装在一个简单的函数中，以便多个模型实例不会共享对同一基础对象的引用
'''
def house_defaults():
    return {'beds': 0, 'baths': 0}

class House(Model):
    number = TextField()
    street = TextField()
    attributes = JSONField(default=house_defaults)
'''
虽然 peewee 未显式提供用于设置服务器端默认值的 API，但您可以使用constraints参数指定服务器默认值
'''    
class Message(Model):
    context = TextField()
    timestamp = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    
    
# 1.3 创建自定义字段类型并将其用于模型
''' 
由于 psycopg2 默认将数据视为字符串，因此我们将向该字段添加两个方法来处理：
db_value:来自我们的python应用程序的数据进入数据库
python_value:从数据库中出来的数据将用于我们的应用程序
'''
import uuid

class UUIDField(Field):
    field_type = 'uuid'

    # 转换 UUID 到 hex string.
    def db_value(self, value):
        return value.hex  

    def python_value(self, value):
        return uuid.UUID(value) # convert hex string to UUID
    



