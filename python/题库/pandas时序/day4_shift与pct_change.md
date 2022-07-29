#### 同比与环比
- 同比指与历史同期做比较,可以避免季节性影响,如2022年7月与2021年7月同比
- 环比指与前一个统计时间段做比较,如2022年7月与2022年6月环比
- (new-old)/old 也即new/old-1
- $$\frac{new-old}{old}=\frac{new}{old}-1$$

#### pandas中对时间索引位移
- 使用shift方法并声明freq参数
- 对于2022-07-29而言,shift(7,freq='D')位移为2022-08-05
- 示例：
```py
df = pd.read_csv(r"BTC.csv",parse_dates=['date'],index_col='date')
df.head(5)

# 计算比特币最高价highp30日周期环比涨幅,请仔细品位这里位移7天而非-7天(时间索引的位移,而非数据帧的位移)
((df.highp-df.highp.shift(30,freq='D'))/df.highp.shift(30,freq='D')).dropna()

# pandas中封装了pct_change方法进行环比统计,与上面自己计算结果一致
df.highp.pct_change(30,freq='D').dropna()#.resample('MS').mean()

```
