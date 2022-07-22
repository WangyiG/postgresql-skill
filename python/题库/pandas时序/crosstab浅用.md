#### 使用crosstab统计百分比
- 白班夜班表现要求不同,统计白班夜班表现百分比
- normalize=True,'index','columns'指定归一化目标
```py
import pandas as pd
import numpy as np

df = pd.read_excel('服务记录.xlsx',parse_dates=['服务发起时间','服务结束时间'],date_parser=lambda x:pd.to_datetime(x,format='%Y年%m月%d日%H点%M分%S秒',errors='coerce'))
df.head()

pd.crosstab((df_ := df.assign(
    班种 = np.where((df.服务发起时间.dt.hour>=8)&(df.服务发起时间.dt.hour<=20),'夜班','白班'),
    耗时 = lambda x:(x.服务结束时间-x.服务发起时间).map(pd.Timedelta.total_seconds)/60,
    表现 = lambda x:np.select(
    [(x.班种=='白班')&(x.耗时<15)|(x.班种=='夜班')&(x.耗时<30),(x.班种=='白班')&(x.耗时>30)|(x.班种=='夜班')&(x.耗时>60)],
    ['优秀','不合格'],
    '合格'
    )
)).班种,df_.表现,margins=True,normalize='index').style.format('{:0.2%}')
```
