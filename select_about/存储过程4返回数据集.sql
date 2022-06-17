create table city (cityId int, cityName varchar(20)); 
insert into city values(1,'BeiJing'),(2,'NewYork'),(3,'Hong kong'),(4,'ShaingHai');

-- setof 表名
/*
return query
返回值既然是个table，那支持where等语句也没问题吧
*/
create or replace function getCity() returns setof city as 
$$
begin
return query select * from city;
end;
$$
language plpgsql;

SELECT getCity()
SELECT * FROM getCity() where cityid>2


-- setof record
/*
动态返回数据集
将表名做为函数参数
return next record_name
返回值为record类型的,调用时应指明字段及字段类型
*/
create or replace function getRows(text) returns setof record as
$$
declare
rec record;
begin
for rec in EXECUTE 'select * from ' || $1 loop
return next rec;
end loop;
return;
end
$$
language 'plpgsql';

SELECT * FROM getRows('city') as city(id int, name varchar(20))

/*游标*/
CREATE TABLE foo (fooid INT, foosubid INT, fooname TEXT);  
INSERT INTO foo VALUES (1, 2, 'three'),(4, 5, 'six');

CREATE OR REPLACE FUNCTION myfunc01() RETURNS SETOF record AS
$$
DECLARE 
  rec_emp RECORD;
  cur_emp CURSOR(id INTEGER) FOR
    SELECT foosubid, fooname 
    FROM foo
    WHERE fooid = id;
BEGIN
  -- 打开游标
  OPEN cur_emp(4);

  LOOP
    -- 获取游标中的记录
    FETCH cur_emp INTO rec_emp;
    -- 没有找到更多数据时退出循环
    EXIT WHEN NOT FOUND;
    RETURN NEXT rec_emp;

    RAISE NOTICE 'When fooid = 4,foosubid = %,fooname = %' , rec_emp.foosubid, rec_emp.fooname;
  END LOOP;

  -- Close the cursor
  CLOSE cur_emp;
END $$ LANGUAGE plpgsql;


SELECT * FROM myfunc01() as foo(foosubid int,fooname text)















