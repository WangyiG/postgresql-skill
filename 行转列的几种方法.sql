-- 先建一个公共表表达式CTE，方便后续演示，其中括号中用的是行表达式
with cte as
(select * from (values('张三','年龄',22),('张三','身高',173),('李四','年龄',20),('李四','身高',181)) as a(name,info,value))

-- 第一种：case when或者filter
select 
name,
sum(case when info = '年龄' then value else 0 end) 年龄,
sum(value) filter (where info = '身高') 身高
from cte
group by name

-- 第二种：string_agg 配合 split_part
select 
name,
(regexp_split_to_array(string_agg(info||':'||value,'-'),'[-:]'))[2] 年龄,    --正则分割，注意括号位置，支持索引取值
split_part( split_part(string_agg(info||':'||value,'-'),':',2),'-',2) 身高   --2次split_part
from cte group by name

select 
name,
(regexp_split_to_array(temp,'[-:]'))[2] 年龄,                                --上面可能看不清，这里string_agg单独拿出来
split_part(split_part(temp,':',2),'-',2) 身高                                —-string_agg内部其实还有个横向concat连接,||
from
(select name,string_agg(info||':'||value,'-') temp from cte group by name)x 

-- 第三种 crosstab(text source_sql,text category_sql)
-- crosstab的安装：终端进入psql，在有create权限的用户下（su mt，输入用户密码postgres），执行create extension tablefunc;
--需要注意的是这里的old_table使用cte报错了，可能是不支持临时表，另外new_table中的数据类型必须准确，否则也会报错
/*
1.crosstab函数为具有相同row_name值的每个连续输入行组生成一个输出行。使用value这些行中的字段从左到右填充输出列。如果组中的行少于输出value列，则额外的输出列将填充空值; 
如果有更多行，则跳过额外的输入行，实际上，SQL查询应始终指定ORDER BY 1,2(这里的1，2是相对位置，select选中的第几个)以确保输入行的顺序正确，即具有相同值的值row_name汇
集在一起并在行中正确排序。类似pivot(name,info,value)
2.当有部分缺失时,crosstab不会聪明的对齐,使用第二个参数也即$$values('字段1'),('字段2')$$,这样才能做到对齐
*/
SELECT *
FROM crosstab('select name, info, value from old_table order by 1,2',$$values('年龄'),('身高')$$)
AS new_table(name varchar, 年龄 int, 身高 int)

SELECT * 
FROM crosstab ('select sid,cid,score from sc order by 1,2',$$values('01'::text),('02'::text),('03'::text)$$ ) 
AS x(sid varchar,a numeric,b numeric,c numeric)

