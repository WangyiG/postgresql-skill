-- 1.创建索引,默认是B-Tree索引,以下2种写法一致

create index idx_name on table_name(column_name,..)
create index idx_name on table_name using btree (column_name)
/*
B-Tree索引主要用于等于和范围查询，特别是当索引列包含操作符" <、<=、=、>=和>"作为查询条件时，PostgreSQL的查询规划器都会考虑使用B-Tree索引。
在使用BETWEEN、IN、IS NULL和IS NOT NULL的查询中，PostgreSQL也可以使用B-Tree索引。然而对于基于模式匹配操作符的查询，如LIKE、ILIKE、~和 ~*，
仅当模式存在一个常量，且该常量位于模式字符串的开头时，如col LIKE 'foo%'或col ~ '^foo'，索引才会生效，否则将会执行全表扫描，如：col LIKE '%bar'。
*/

-- 2.hash索引

create index idx_name on table_name using hash (column_name)

/*
散列(Hash)索引只能处理简单的等于比较。当索引列使用等于操作符进行比较时，查询规划器会考虑使用散列索引。
这里需要额外说明的是，PostgreSQL散列索引的性能不比B-Tree索引强，但是散列索引的尺寸和构造时间则更差。
另外，由于散列索引操作目前没有记录WAL日志，因此一旦发生了数据库崩溃，我们将不得不用REINDEX重建散列索引。
*/

-- 3.GiST索引

create index idx_name on table_name using gist ( int8range(beginid,endid,'[)') )

/*
示例中表示创建左开右闭的范围索引
GiST索引不是一种单独的索引类型，而是一种架构，可以在该架构上实现很多不同的索引策略。从而可以使GiST索引根据不同的索引策略，而使用特定的操作符类型
*/

-- 4.GIN索引

create index idx_name on table_name using gin (xxx)

/*
GIN索引是反转索引，它可以处理包含多个键的值(比如数组)。与GiST类似，GIN同样支持用户定义的索引策略，从而可以使GIN索引根据不同的索引策略，而使用特定的操作符类型。
作为示例，PostgreSQL的标准发布中包含了用于一维数组的GIN操作符类型，如：<@、@>、=、&&等。
*/

-- 5.事务,事务将多步操作看着一个单元,要么都做,要么都不,语法为begin;xxx;commit;

BEGIN;
-- Alice的账户余额减去100.00
UPDATE accounts SET balance = balance - 100.00
    WHERE name = 'Alice';
-- Alice所在分行总余额减去100.00
UPDATE branches SET balance = balance - 100.00
    WHERE name = (SELECT branch_name FROM accounts WHERE name = 'Alice');
-- Bob的账户余额加上100.00
UPDATE accounts SET balance = balance + 100.00
    WHERE name = 'Bob';
-- Bob所在分行总余额加上100.00
UPDATE branches SET balance = balance + 100.00
    WHERE name = (SELECT branch_name FROM accounts WHERE name = 'Bob');
COMMIT;

-- 6.事务的SAVEPOINT,完成一关创建一个复活点还不明白吗？确定没问题之后再commit

/*在比较大的事务中，可以把执行过程分为几个步骤，每个步骤执行完成后创建一个保存点，后续步骤执行失败时，可回滚到之前的保存点，而不必回滚整个事务。
假定从 Alice 的账号给 Bob 的账号打 100.00 块钱，后来才发现收款人应是 Wally。*/

BEGIN;
UPDATE accounts SET balance = balance - 100.00
    WHERE name = 'Alice';
SAVEPOINT my_savepoint;
UPDATE accounts SET balance = balance + 100.00
    WHERE name = 'Bob';
-- oops ... forget that and use Wally's account
ROLLBACK TO my_savepoint;
UPDATE accounts SET balance = balance + 100.00
    WHERE name = 'Wally';
COMMIT;

-- 7.若查询涉及多个窗口函数，可以将WINDOW子句抽出来，window是一个关键字，用法和index as，table as 一样呗，只是接在表名后不用写create罢了

select 
avg(info) over w, 
sum(info) over w 
from (values(1,1),(1,2),(2,3),(2,4)) as t(id,info) window w as (partition by id)

-- 8.表继承，查询父表时，会把这个父表中子表的数据也查询出来，反之则不行，如果只想把父表本身的数据查询出来，需要在父表名前加ONLY

create table city as select * from (values(1,'常州'),(2,'芜湖')) as t(id,name)
create table shenghui(id int,name text) inherits (city)
insert into shenghui values(3,'合肥'),(4,'南京')

select * from city                -- 查出城市及省会表中的全部城市

select * from shenghui            -- 查出仅在省会表中的

select * from only city           -- 查出仅在城市表中的
    
