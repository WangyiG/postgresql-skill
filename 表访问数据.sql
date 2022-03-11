1.公共表表达式CTE,临时表

-- with a as (select * from (values (1,2),(2,3),(3,4),(4,100),(2,101),(101,104),(3,102),(4,103),(103,105)) as t(id1,id2)),
        b as (select * from (values (1,2),(2,3),(3,4),(4,100),(2,101),(101,104),(3,102),(4,103),(103,105)) as x(id3,id4))
   select * from a join b on a.id1 = b.id3
   
2.select语句,随机排序,位移

-- select col_name from table_name order by random() limit 3

-- select  col_name from table_name order by order_col offset 2 limit 3

3.行表达式

-- select * from (values(1,'test1'),(2,'test2'),(3,'test3')) as t(id, info)
