--  一些序列

--  基于表的数字辅助列,便于over开窗使用，或直接辅助排序

select num_start,generate_series(0,num_end-num_start)+num_start explode from (values(1,3),(4,7)) as x(num_start,num_end)
