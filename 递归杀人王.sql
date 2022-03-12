-- 1.数据准备,观察这里的原始数据,5-6-8-5存在闭环,即死循环,注意学习大佬们是如何处理的

CREATE TABLE sys_cbp_test (id INT,parent_id INT);

INSERT INTO sys_cbp_test VALUES(1, NULL),(2, 1),(3, 2),(4, 3),(5, 1),(6, 5),(7, 2),(8, 6),(5, 8),(20, NULL),(21, 20),(22, 21);

-- 2.原始数据只有2列,为了理清关联,需要理清节点层级、起始节点、节点路径、是否存在死循环、是否叶子节点等

with recursive x(
id,                             -- 节点id
parent_id,                      -- 父节点id
level,                          -- 节点层级
path,                           -- 节点路径
root,                           -- 起始节点
cycle                           -- 节点是否循环  
) as 

/*
与正常简单的with cte as开局不同,这里直接声明需要的6个字段,下面非递归语句中使用了标量1和False,定义好列名后才方便后续递归使用
*/

(
/*起始非递归语句*/
select id,parent_id,1,array[id],id as root,False from sys_cbp_test where parent_id is null

union all

/*递归循环语句开始*/
SELECT 
b.id,
b.parent_id,
level + 1,                      --递归一层节点层级加1
x.path || b.id,                 --把节点按照递归的次序依次存入数组
x.root,                         --记录起始节点
b.id = ANY(path)                --判断当前节点是否已存在路径数组中，如果存在说明存在循环

FROM x,sys_cbp_test b
WHERE x.id = b.parent_id        --从起始节点往下递归
AND NOT cycle                   --终止循环节点,去掉循环重复的节点，反过来也可以查找哪个节点存在死循环
)

--3.递归结束,开始有条理且完整的展示数据
select
id,
x.parent_id,
level,
array_to_string(path, '->') AS path,
root,
path,
cycle,
case when y.parent_id is null then True else False end as isleaf  --是否叶子节点

from x 
left join (select parent_id from sys_cbp_test group by parent_id) y
on x.id = y.parent_id
order by id
