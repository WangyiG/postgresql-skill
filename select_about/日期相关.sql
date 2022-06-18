-- 获取当前日期
select current_date

-- 在date基础上+年月日,写month，主要为了区分Minute，其中interval时间差可以省略
select current_date + interval '1 Y'
select current_date + interval '1 Month'
select current_date + interval '1 D'

-- age函数返回 {'years':m,'months':n,'days':k}
select age(current_date,'1993-08-28')

-- extract函数(field from source)其中source必须是timestamp、time、interval类型的值表达式。field是一个标识符或字符串，是从源数据中的抽取的域。
select extract(year from age(current_date,'1993-08-28')) -- 返回28周岁
select extract(year from current_date) -- 返回2022年

-- postgresql中的时间数据类型
timestamp --包括日期和时间，默认无时区
date      --日期，不包括时间
time      --只有时间没有日期，默认无时区
interval  --时间间隔
