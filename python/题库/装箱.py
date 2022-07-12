import pandas as pd

df = pd.DataFrame({'规格型号':['19.5D','20.0D','20.5D','21.0D','21.5D','22.0D'],'数量':[108,160,142,132,170,140]})
df

# 要求:已知每个箱子能装162个,要求把分箱装完材料,每个箱子装满162个,剩余数量装另一个箱子
df1 = df.规格型号.repeat(df.数量).reset_index(drop=True)
df1

df1.groupby((df1.index//162+1).astype('str')+'号箱').apply(pd.Series.value_counts).reset_index().set_axis(['箱号','规格型号','数量'],axis=1)
