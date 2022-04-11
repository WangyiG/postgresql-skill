df = pd.read_excel('/Users/mt/Desktop/新增与留存.xlsx')

(df.assign(首登=df.groupby('用户ID').日期.transform('first'),
           留存=lambda x:x.日期.dt.day-x.首登.dt.day,
           连续=lambda x:x.留存-x.groupby('用户ID').cumcount())
   .query('连续<=0')
   .assign(留存=lambda x:x.留存.map(lambda n:f'第{n}日留存' if n else '首日新增'))
   .groupby(['首登','留存'])
   .用户ID.nunique()
   .unstack()
   .fillna('')).iloc[:,[4,0,1,2,3]]
