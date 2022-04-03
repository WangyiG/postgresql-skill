 -- install
 brew install postgresql@14 

 -- 查看版本,确认已安装
 pg_ctl -V
 
 -- 初始化数据库,mt为实际的电脑用户名
 initdb -D /Users/mt/other/postgresql -U mt --lc-collate=C --lc-ctype=en_US.UTF-8 --lc-messages=en_US.UTF-8 -E UTF8 
 initdb -D /Users/mt/other/postgresql -U mt --lc-collate=zh_CN.UTF-8 --lc-ctype=zh_CN.UTF-8 --lc-messages=zh_CN.UTF-8 -E UTF8 
 
 -- 如果是重新安装，初始化提示，之前文件夹已存在，需要重建路径或先删除原路径
 rm -rf /Users/mt/other/postgresql
 
 -- 启动数据库
 pg_ctl -D /Users/mt/other/postgresql  start
 
 -- 需要先执行createdb，然后才能psql进入控制台
 
 -- https://www.jianshu.com/p/e7bc2ea02c5c
 
 -- 后台启动postgresql
 brew services start postgresql
 
 -- 前台启动
 postgres -D /usr/local/var/postgres
 
 -- 停止postgresql
 brew services stop postgresql
 
 -- 重启postgresql
 brew services restart postgresql
 
 -- mac重启后数据还原,操作步骤
 1.brew services restart postgresql
 2.createdb,psql,\l
 3.create mydb,执行还原
 
 -- 并行设置,show查看最大可设置值m,set设置n，n小于等于m，set设置强制并行为on：
SHOW max_worker_processes

SHOW max_parallel_workers_per_gather
SET max_parallel_workers_per_gather = 8

SHOW parallel_setup_cost
SET parallel_setup_cost = 0

SHOW parallel_tuple_cost
SET parallel_tuple_cost = 0

SHOW force_parallel_mode
SET force_parallel_mode = on

alter table tbao set (parallel_workers=8);
 
 https://github.com/digoal/blog/blob/61bbe29d6f06bb9b98b7a694f2180ffd33987835/201812/20181218_01.md

/*
终端进入数据库编辑模式：psql
查看有哪些数据库：\l
切换数据库：\c dbname
退出psql控制台编辑模式：\q
指定某用户连接某数据库：psql -U postgres -d postgres
统计用时：\timing
\d test --查看表的结构，类似df.info()
*/

CREATE USER postgres WITH PASSWORD 'postgres'; -- 创建用户、密码（注意引号）

CREATE DATABASE dbname OWNER username; -- 为某个user创建dbname

DROP DATABASE dbname; -- 删除数据库

ALTER ROLE username CREATEDB; --允许某用户创建数据库

GRANT ALL PRIVILEGES ON DATABASE postgres to postgres; --授权postgres用户从任何主机连接postgres数据库



-- topn插件安装
git clone https://github.com/citusdata/postgresql-topn  
cd postgresql-topn  
USE_PGXS=1 make  
USE_PGXS=1 make install

进入psql，在psql中:create extension topn;

精度建议设置为10000
load 'topn';
show topn.number_of_counters ;
set topn.number_of_counters =10000;

