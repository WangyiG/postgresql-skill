```py
import pandas as pd

df = pd.read_csv(r"C:\Users\wangy\Desktop\user_info.csv",parse_dates=['register_time','recently_logged'],date_parser=lambda x:pd.to_datetime(x,errors='coerce'))
df.head(3)

# 在当月进行注册的用户中,learn_time最长的用户其user_id及对应的learn_time信息
# 排序处理,注意groupby中的sort参数是分组聚合后对结果排序,而非组中排序
df.dropna(subset='register_time').sort_values('learn_time').groupby(df.register_time.dt.to_period('m')).last().iloc[:,[0,4]]

# resample的apply本质是agg,按列传入而非整个df传入
df.dropna(subset='register_time').resample('MS',on = 'register_time').apply(lambda x:pd.DataFrame(x).sort_values('learn_time').tail(1).iloc[:,[0,4]])


# 统计当月流水与非当月流失数及占比情况,其中当月流失指注册年月与最近登录年月一致

(
    df.dropna(subset=['register_time','recently_logged'])
      .assign(
        流失情况 = lambda x:x.register_time.dt.to_period('m').eq(x.recently_logged.dt.strftime('%Y-%m'))
             )
      .groupby(pd.Grouper(key='register_time',freq='MS'))
      .agg(
            当月流失 = ('流失情况','sum'),
            非当月流失 = ('流失情况',lambda x:x.count()-x.sum()),
            当月流失率 = ('流失情况',lambda x:x.sum()/x.count()),
            非当月流失率 = ('流失情况',lambda x:1-x.sum()/x.count()),
          )
      .sort_values('当月流失率',ascending=False)
      .reset_index()
      .style
      .format(
            {
                'register_time':'{:%F}',
                '当月流失率':'{:.2%}',
                '非当月流失率':'{:.2%}',
            }
        )
) 
```
