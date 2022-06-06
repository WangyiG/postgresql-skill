#  导入相关库

import uuid
import orjson
import numpy as np
from datetime import datetime
from dataclasses import dataclass

#  准备一个自定义数据类,方便后续使用

@dataclass
class User:
    id:str
    phone_number:int
      
demo_json = {'a':'b','c':{'d':True},'e':[1,2]}      

#  2进制序列化,可使用decode解码

json1 = orjson.dumps(demo_json)
type(json1),json1.decode()

#  反序列化

orjson.loads(json1)


## 丰富的option选项

# orjson.OPT_INDENT_2为序列化后的JSON结果添加2个空格的缩进及换行

print(orjson.dumps(demo_json,option=orjson.OPT_INDENT_2).decode())

# orjson支持将标准库中的时间日期对象转换成相应的字符串,orjson.OPT_OMIT_MICROSECONDS支持将转换结果后缀的毫秒部分省略掉

orjson.dumps({'now':datetime.now()}).decode(),orjson.dumps({'now':datetime.now()},option=orjson.OPT_OMIT_MICROSECONDS).decode()

# orjson.OPT_NON_STR_KEYS将数值类型的键转换为字符类型。对于多种option选项组合,使用|或标识符连接

print(orjson.dumps(dict(zip([1,2],['a','b'])),option=orjson.OPT_NON_STR_KEYS|orjson.OPT_INDENT_2).decode())

# orjson.OPT_SERIALIZE_NUMPY支持将包含numpy中数据结构对象的复杂对象，兼容性地转换为JSON中的数组

orjson.dumps({'numpy_array':np.arange(9).reshape(3,-1)},option=orjson.OPT_SERIALIZE_NUMPY)

## 部分option选项可与default参数联动使用,对option选项指定的对象,执行default参数指定的函数

#  orjson.OPT_PASSTHROUGH_DATACLASS指定自定义的dataclass的实例，执行default参数指定的函数

f = lambda obj:{'id':obj.id,'phone_number':f'{str(obj.phone_number)[:3]}xxx{str(obj.phone_number)[-4:]}'}

demo_json1 = {'user1':{'id':'test','phone_number':13666666666},'user2':User(id=str(uuid.uuid4()),phone_number=13888888888)}

orjson.dumps(demo_json1,option=orjson.OPT_PASSTHROUGH_DATACLASS,default=f)

# orjson.OPT_PASSTHROUGH_DATETIME指定datetime实例,执行default参数指定的函数

g = lambda obj:obj.strftime('%Y年%m月%d日')

orjson.dumps({'now':datetime.now()},option=orjson.OPT_PASSTHROUGH_DATETIME,default=g).decode()

# 当存在不同类型的对象时,default参数调用的函数应当能分而治之

demo_json2 = {'now':datetime.now(),'user':User(id=str(uuid.uuid4()),phone_number=13888888888)}

def func(obj):
    if isinstance(obj,datetime):
        return g(obj)
    if isinstance(obj,User):
        return f(obj)

orjson.dumps(demo_json2,option=orjson.OPT_PASSTHROUGH_DATETIME|orjson.OPT_PASSTHROUGH_DATACLASS,default=func).decode()





