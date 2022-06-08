# 为了不污染模型命名空间，特定于模型的配置被放置在一个名为Meta的特殊类中
from peewee import *

db = PostgresqlDatabase('peewee_test', user='postgres', password='postgres',host='127.0.0.1')


class BaseModel(Model):
    class Meta:
        database = db

class Person(BaseModel):
    name = CharField()
    
        
# 该类实现了几种方法，这些方法可用于检索模型元数据（如字段列表、外键关系等）,通过Person._meta.方法来访问
# 有几个选项可以指定为属性。虽然大多数选项都是可继承的，但有些选项是特定于表的，不会被子类继承
{
  database : 模型数据库，可被继承，
  table_name : 表名，特定于表的属性，不可被继承，
  table_function ： 动态表名生成函数，因为是动态的，可被继承，
  indexes ： 要编制索引的字段列表，可被继承，
  primary_key ： 主键，可被继承，
  constraint ： 约束，可被继承，
}

# Meta类方法示例
# primary_key，设置复合主键与指定模型没有主键(不自动生成自增的id列)
class BlogToTag(Model):
    blog = ForeignKeyField(Blog)
    tag = ForeignKeyField(Tag)

    class Meta:
        primary_key = CompositeKey('blog', 'tag')

class NoPrimaryKey(Model):
    data = IntegerField()

    class Meta:
        primary_key = False
        

# table_function，动态表名生成函数
def make_table_name(model_class):
    model_name = model_class.__name__
    return model_name.lower() + '_tbl'

class BaseModel(Model):
    class Meta:
        table_function = make_table_name

class User(BaseModel):
    # table_name will be "user_tbl".

class UserProfile(BaseModel):
    # table_name will be "userprofile_tbl"

    
# 简单的单列索引与约束是通过传参给Field类实现
class Product(BaseModel):
    name = CharField(unique=True)
    price = DecimalField(constraints=[Check('price < 10000')])
    created = DateTimeField(constraints=[SQL("DEFAULT (datetime('now'))")])
    

# 也可以使用嵌套元组将多列索引定义为 Meta 属性。每个数据库索引都是一个 2 元组，其第一部分是字段名称的元组，第二部分是指示索引是否应唯一的布尔值
class Transaction(Model):
    from_acct = CharField()
    to_acct = CharField()
    amount = DecimalField()
    date = DateTimeField()

    class Meta:
        indexes = (
            # create a unique on from/to/date
            (('from_acct', 'to_acct', 'date'), True),

            # create a non-unique on from/to
            (('from_acct', 'to_acct'), False),
        )
        
# 如果索引元组仅包含一个项目，请记住添加尾随逗号
class Meta:
    indexes = (
        (('first_name', 'last_name'), True),  # Note the trailing comma!
    )
    
    
# Peewee 支持更结构化的 API，用于使用 Model.add_index（） 方法或直接使用 ModelIndex 帮助程序类在模型上声明索引
class Article(Model):
    name = TextField()
    timestamp = TimestampField()
    status = IntegerField()
    flags = IntegerField()

# Add an index on "name" and "timestamp" columns.
Article.add_index(Article.name, Article.timestamp)

# Add a partial index on name and timestamp where status = 1.
Article.add_index(Article.name, Article.timestamp,
                  where=(Article.status == 1))

# Create a unique index on timestamp desc, status & 4.
idx = Article.index(
    Article.timestamp.desc(),
    Article.flags.bin_and(4),
    unique=True)
Article.add_index(idx)
        
        
# 表约束 
# 假设有一个人员表，其中包含两列（该人员的名字和姓氏）的复合主键。您希望另一个表与 people 表相关，为此，需要定义一个外键约束
class Person(Model):
    first = CharField()
    last = CharField()

    class Meta:
        primary_key = CompositeKey('first', 'last')

class Pet(Model):
    owner_first = CharField()
    owner_last = CharField()
    pet_name = CharField()

    class Meta:
        constraints = [SQL('FOREIGN KEY(owner_first, owner_last) '
                           'REFERENCES person(first, last)')]
        
        
# Peewee对复合键有非常基本的支持。要使用复合键，必须将模型选项的属性设置为复合键实例
class BlogToTag(Model):
    """A simple "through" table for many-to-many relationship."""
    blog = ForeignKeyField(Blog)
    tag = ForeignKeyField(Tag)

    class Meta:
        primary_key = CompositeKey('blog', 'tag')
        
        
        
        
        
        
        
        
