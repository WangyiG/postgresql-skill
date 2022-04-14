df = pd.DataFrame({'日期':['1日','2日','1日','2日'],'姓名':['小王','小明','小张','小王'],'成绩':['优秀','优秀','良好','一般']})

#sql解法:

select coalesce(日期,'总计') 日期,sum(case when 成绩 = '优秀' then 1 else 0 end)*1.0/count(distinct 姓名) 优秀占比 from m group by rollup(日期);

#pd解法：

pd.pivot_table(df,['姓名','成绩'],'日期',aggfunc={'姓名':'nunique','成绩':lambda x:x.eq('优秀').sum()},margins=True,margins_name='合计').eval('优秀占比=成绩/姓名')

pd.concat([df,df.assign(日期='合计')]).groupby('日期').agg({'姓名':'nunique','成绩':lambda x:x.eq('优秀').sum()}).eval('优秀占比=成绩/姓名')
