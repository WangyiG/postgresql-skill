-- 触发器概述
/*
触发器（trigger）是一种特殊的函数,当某个数据变更事件(INSERT\UPDATE\DELETE\TRUNCATE)或者数据库事件(DDL语句)发生时自动执行.
触发器种类，其中第一种更常见：
1.基于某个表或者视图数据变更的触发器被称为数据变更触发器(DML 触发器).
2.基于数据库事件的触发器被称为事件触发器(DDL 触发器).
触发方式:
1.行级（row-level）触发器
2.语句级（statement-level）触发器
区别在于触发的时机和触发次数。例如，对于一个影响 20 行数据的 UPDATE 语句，行级触发器将会触发器 20 次，而语句级触发器只会触发 1 次

触发器可能带来的问题是:在不清楚它们的存在和逻辑时可能会影响数据修改的结果和性能.
*/

-- 触发器的创建
/*
1.使用 CREATE FUNCTION 语句创建一个触发器函数；
当自定义函数的返回类型设置为trigger时,说明是一个触发器函数,触发器函数不需要参数,因为触发器内部系统自定义了许多内部参数：
new :record类型,表示行级触发器insert/update操作之后的新数据行,对于delete操作或语句级触发器而言,该变量为Null
old: record类型,表示行级触发器update/delete操作之前的旧数据行,对于insert操作或语句级触发器而言,该变量为Null
tg_name :触发器名称，触发器函数可能关联多个trigger
tg_when :触发时机,如before/after/instead of
tg_level :触发级别,row级或statement级
tg_op :触发的操作，insert/update/delete/truncate
tg_relid :触发器所在表的oid
tg_table_name :触发器所在表的名称
tg_table_schema :触发器所在表的模式
tg_nargs :创建触发器时给触发器函数传递的参数个数
tg_argv[] :创建触发器时传递给触发器函数的具体参数,下标从0开始,非法下标则返回Null
*/


CREATE TABLE fruits(id serial,fruit_id int,name text,quantity int,price int , money int)

INSERT INTO fruits(fruit_id,name, quantity,price,money) VALUES (1,'apple',10,6,60),(2,'orange',15,5,75),(3,'banana',12,4,48),(4,'peach',11,7,77)

-- 创建2个表，表示入库与出库，fruit_in,fruit_out

CREATE TABLE fruit_in(id serial,fruit_id int,name text,quantity int,price int , money int)

CREATE TABLE fruit_out(id serial,fruit_id int,name text,quantity int,price int , money int)

-- 创建入库触发器函数
create or replace function in_change()
  returns trigger as
$$
begin
  if tg_op = 'INSERT' then
    UPDATE fruits set 
    quantity = quantity + new.quantity,
    money = money + new.money,
    price = (money + new.money)/(quantity + new.quantity)
    where fruit_id = new.fruit_id;
  end if;
  return new;
end; 
$$ language plpgsql;

-- 创建触发器并与入库表关联
create trigger trg_in_change
  before insert or update or delete
  on fruit_in
  for each row
  execute function in_change();

-- 给入库表插入数据,查看fruits总表的变化
INSERT INTO fruit_in(fruit_id,name, quantity,price,money) VALUES (1,'apple',10,6,60),(2,'orange',15,5,75),(3,'banana',12,4,48),(4,'peach',11,7,77)

-- 创建出库触发器函数
create or replace function out_change()
  returns trigger as
$$
begin
  if tg_op = 'INSERT' then
    UPDATE fruits set 
    quantity = quantity - new.quantity,
    money = money - new.money,
    price = (money - new.money)/(quantity - new.quantity)
    where fruit_id = new.fruit_id;
  end if;

  return new;
end; 
$$ language plpgsql;

-- 创建触发器并与出库表关联
create trigger trg_out_change
  before insert or update or delete
  on fruit_out
  for each row
  execute function out_change();

-- 给出库表插入数据,查看fruits总表的变化
INSERT INTO fruit_out(fruit_id,name, quantity,price,money) VALUES (1,'apple',10,9,90),(2,'orange',20,6,120),(3,'banana',14,4,56),(4,'peach',12,10,120)


-- 需要先删除触发器
DROP TRIGGER trg_in_change on fruit_in
DROP TRIGGER trg_out_change on fruit_out

-- 才能删除触发器函数
DROP FUNCTION in_change,out_change
  
--  删除表格
DROP table fruits,fruit_in,fruit_out  
























