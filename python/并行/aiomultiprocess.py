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




