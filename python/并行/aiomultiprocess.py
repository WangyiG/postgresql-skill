# 新建functest.py

import json
import pandas as pd

async def f(x):
    with open(x,'r',encoding='utf-8') as fs:
        res = []
        for f in fs:
            res.append(json.loads(f.strip()))
    return pd.DataFrame(res).query('name=="张三"')

async def g(x):
    m = await f(x)
    return m
  

# 新ipynb文件中
# 实测1000个txt文件，每行格式均为{name:xxx,timestamp:xxx,content:xxx}，合计25G,查找其中姓名为张三的，耗时24秒。
import pandas as pd
from aiomultiprocess import Pool 
import asyncio
import json
from functest import g
from glob import glob

paths = glob('/Users/mt/Documents/python/群友题解/IO数据/records/*.txt')

res_ = []
async def main():
    async with Pool() as pool:
        async for res in pool.map(g,paths):
            res_.append(res)
await main()

pd.concat(res_)



# 实现异步上下文,在__aenter__中返回的结果才是上下文结果
class File():
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode

    async def to_do(self):
        self.f = open(self.filename,self.mode,encoding='utf-8')
        res = []
        for f in self.f:
            res.append(json.loads(f.strip()))
        return pd.DataFrame(res).query('name=="张三"')

    async def __aenter__(self):
        self.v = await self.to_do()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        self.f.close()

async def func(x):
    async with File(x,'r') as fs:
       res = fs.v
    return res

# await func(x)



