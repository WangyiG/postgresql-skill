--filter子句的出现是为了简化case when子句
select 聚合函数 filter (where 条件) from table_name

-- 跟表一样长的数字辅助列
select row_number() over (order by 0) idx,* from table_name

-- 创建一个近3天的时间列，注意这里减的是2天，利用::date转换成年月日的形式
-- 如果这样的话，他会生成一个3*3共9行的表，类似日期区间会被explode
select generate_series(current_date-interval '2 D',current_date,'1 D')::date as time,cid from course

-- 可以利用join去拼接上，变成辅助列
(select generate_series(current_date-interval '2 D',current_date,'1 D')::date as time) alias_name left join table_name

--生成某个时间区间
select to_char(generate_series(to_date('2018-01-01','yyyy-mm-dd'),to_date('2020-01-01','yyyy-mm-dd'),'7 D'),'yyyy-mm-dd') as time

-- 返回第一个非空参数
-- 假设现在有some_col varchar，4行分别为‘a'，’b'，‘’，‘d’
select coalesce(some_col,'no word') as new_col from table_name;
-- 第一行第一个非空为‘a’，第二行第一个非空为‘b’，第三行第一个非空为‘no word’

-- 假设现在有some_col int4，4行分别为1，2，，4
-- 注意some_col的类型
select coalesce(some_col,0) as new_col from table_name;

-- rank排序[1,1,2,3]会排1，1，3，4
select rank() over (partition by 分组列 order by 排序列)

-- dense_rank排序[1,1,2,3]会排1，1，2,3
select dense_rank() over (partition by 分组列 order by 排序列)

-- row_number排序[1,1,2,3]会排1，2，3，4
select row_number() over (partition by 分组列 order by 排序列)

-- 对每组聚合，并聚合分组后结果
-- eg：{1:[1,3],2:[2,4],3:[3,5]} 进行avg返回 {1:2,2:3,3:4,null:3}
select col_name,avg(another_col_name) from table_name group by rollup(col_name)
