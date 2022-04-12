# pd实现
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

# sql实现
select 
      首登,
      max(num) filter(where 留存=0) 首日新增,
      max(num) filter(where 留存=1) 第1日留存,
      max(num) filter(where 留存=2) 第2日留存,
      max(num) filter(where 留存=3) 第3日留存,
      max(num) filter(where 留存=4) 第4日留存
from 
     (select 
           首登,
     	留存,
     	count(distinct id) num 
       from
           (select 
         	      *,
         	      first_value(date) over w 首登,
         	      date-first_value(date) over w 留存,
         	      row_number() over w -1 连续 
             from 
         	      load_user window w as (partition by id order by date)) t
       where 留存 = 连续
       group by 首登,留存) m
group by 首登


