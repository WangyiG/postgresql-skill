### EMA
- 滑动平均:以指数式递减加权的移动平均，各数值的加权影响力随时间呈指数式递减，时间越靠近当前时刻的数据加权影响力越
- 时间比较久远的变量值的影响力相对较低，时间比较远的全量值的影响力相对较高
- 演化:算术平均(权重相等) - 加权平均(权重不等) - 移动平均(只取最近的N次数据进行权重相等或不等的计算) - 批量归一化(BN)及各种优化算法的基础
- 缺失值填充的比较
```sh
rolling进行移动平均值填充
- 如window=10时,前9位填充设置min_periods
- 每个元素权重相同
ema进行滑动平均填充
- 各数值的加权而随时间而指数式递减，越近期的数据加权越重
- 递推求值
```
### pandas中ewm
- ewm(com=None, span=None, halflife=None, alpha=None, min_periods=0, adjust=True, ignore_na=False, axis=0, times=None, method='single')
- 参数解析：





- 必须在质心(com)、跨度(span)、半衰期(half-life)和alpha中选择一个来指定衰减系数α
- 衰减系数α确定后,通过adjust配置加权平均值的计算方式
```sh
1.adjust = True(默认):
使用权重(1-α)^(n-1), (1-α)^(n-2),...1-α, 1来计算加权平均值。

2.adjust = False:
使用如下递归计算加权平均值：
weightd_average[0] = arg[0];
weighted_avreaged[i] = (1-α) * weighted_average[i-1] + α * arg[i]
```
｜参数｜类型｜可选或有默认值｜说明｜
｜---｜---｜---｜---｜
｜com｜float｜可选｜根据质心指定衰减，α=1/(1+com),其中com ≥ 0｜
｜span｜float｜可选｜根据范围指定衰减，α=2/(span+1), 其中span ≥ 1｜



｜halflife|float|可选|根据半衰期指定衰减|α=1−exp(log(0.5)/halflife), 其中halflife > 0｜
|alpha|float|可选|指定平滑系数α，其中0<α≤1｜
|min_periods|int|默认为0|窗口中具有值的最小观察数(否则结果为NA)｜
|adjust|bool|默认为True|除以开始阶段的衰减调整因子，以解释相对权重的不平衡(将EWMA视为移动平均线)｜
|ignore_na|bool|默认为False|权重基于绝对值位置,如果为True则权重基于相对值位置|
|axis|{0或者'index'，1或‘columns’}|默认为0|0标识行，1标识列|
|method|single或table|默认为single|单轴或整表滚动,仅在指定engine='numba'时实现且仅适用于mean()|
