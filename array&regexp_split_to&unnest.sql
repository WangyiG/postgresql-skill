-- 1. 数组合并

select array[7,9]||8                                       -- [7,9,8]

select array['a','c']||array['b']                          -- 数组元素为字符时，后面的array需要写,['a','c','b']

-- 2.数组支持索引，从1开始的索引

select (array['a','c']||array['b'])[2]                     -- 'c'

-- 3.数组拼接成字符

select array_to_string((array[7,9]||8),'~^~')              -- '7~^~9~^~8'

-- 4.字符串切割成数组

select string_to_array('I-loveing-you!','-')               -- ['I','loving','you!']

select regexp_split_to_array('I-loveing-you!','i*n*g*-')   -- ['I','love','you!'],正则学的比较差，按-或ing-分隔写的比较烂

select regexp_split_to_array('I-loveing-you!','-|ing-')    -- ['I','love','you!'],正则重写一下


-- 5.字符串切割成一列

select regexp_split_to_table('I-loveing-you!','-|ing-')

select unnest(string_to_array('I-loveing-you!','-'))

-- with ordinality 必须接在from子句的函数后面使用
select ordinality id,unnest info from unnest(string_to_array('I-loveing-you!','-')) with ordinality  -- 通过unnest(array) with  ordinality增加编号

--6.any,all与array的搭配使用
/*
创建cte方便测试
with x as (select * from (values(1,3),(2,6)) as t(id,info))
*/

select * from x where info > any(array[2,4])

select * from x where info > all(array[2,4])

select *,info>all(array[2,4]) from x 
