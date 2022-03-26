# 导入相关包
 import pandas as pd
 import psycopg2
 from sqlalchemy import create_engine
 from io import StringIO
 from io import BytesIO

 # 读取csv文件并设置列名,engine='pyarrow'可加速读取
 df = pd.read_csv("UserBehavior.csv",header=None,names=['user_id','item_id','category_id','behavior_type','timestamp'],engine='pyarrow')
  
 # 检查空值
 df.isna().sum()
  
 # 去重
 df = df.drop_duplicates(subset=['user_id','item_id','timestamp'])

 # 新增时间相关列
 df = df.copy()
 df['datetimes'] = pd.to_datetime(df.timestamp,unit='s')
 df['dates'] = df.datetimes.dt.date
 df['times'] = df.datetimes.dt.time
 df['hours'] = df.datetimes.dt.hour
 df.head()

 # 取出列名备用
 col = df.columns

 # 把dataframe读入内存
 output = StringIO()
 df.to_csv(output, sep='\t', index=False, header=False)
 output1 = output.getvalue()

 # 把数据写入数据库
 # 需要先建表:create table tbao(user_id int,item_id int,category_id int,behavior_type varchar,timestamp int,datetimes timestamp,dates date,times time,hours int)
 conn = psycopg2.connect(host='localhost', user='mt', password='postgres', database='mydb')
 cur = conn.cursor()
 cur.copy_from(StringIO(output1),'public.tbao',null='',columns=col)
 conn.commit()
 cur.close()
 conn.close()
 print('done')
