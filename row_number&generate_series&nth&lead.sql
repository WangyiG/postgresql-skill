1. 基于表的数字辅助列,便于over开窗使用，或直接辅助排序

- row_number() over (order by 0),生成1,2,3,4...n

- rank() over (order by 0),生成1,1,1,1...1

2. generate_series()函数,非基于表,即需要join拼接去使用,否则会起到爆炸explode效果

- select generate_series(1,2) as m,generate_series(1,5,2) as n,生成m列1,2,null,生成n列1,3,5

- select generate_series(current_date-interval '6 D',current_date,'1 D')::date as recent_7_day,生成最近7天,如示例所示类型转换::date可以接在generate_series后面

- select num_start,generate_series(0,num_end-num_start)+num_start from (values(1,3),(4,7)) as x(num_start,num_end),可利用特性实现explode效果

3.first_value(),last_value(),nth_value() 聚合函数,需要搭配over使用，不使用order by 则基于原始行取值，有点fillna(nth_value)的感觉

- select *,nth_value(v,2) over (partition by id) from (values(1,3),(1,1),(1,2),(2,5),(2,6),(2,4)) as x(id,v)

4.lead(col_name,step,fillna_value)向上偏移,lag(col_name,step,fillna_value)向下偏移,这2个偏移函数需要配合over()使用，其中partition无时以整个表做为分区

- select *,lead(v,1,0) over (partition by id) from (values(1,3),(1,1),(1,2),(2,5),(2,6),(2,4)) as x(id,v)

- select *,lag(v,1,0) over (partition by id) from (values(1,3),(1,1),(1,2),(2,5),(2,6),(2,4)) as x(id,v)

- select *,lead(v,1,0) over () from (values(1,3),(1,1),(1,2),(2,5),(2,6),(2,4)) as x(id,v)
