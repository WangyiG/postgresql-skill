-- 1.游标
/*
游标允许我们封装一个查询，然后每次处理结果集中的一条记录。游标可以将大结果集拆分成许多小的记录，避免内存溢出；
另外，我们可以定义一个返回游标引用的函数，然后调用程序可以基于这个引用处理返回的结果集
使用游标的步骤大体如下：
1.声明游标变量；
2.打开游标；
3.从游标中获取结果；
4.判断是否存在更多结果。如果存在，执行第 3 步；否则，执行第 5 步；
5.关闭游标
*/
CREATE TABLE foo (fooid INT, foosubid INT, fooname TEXT);  
INSERT INTO foo VALUES (1, 2, 'three');  
INSERT INTO foo VALUES (4, 5, 'six'); 

DO $$
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

    RAISE NOTICE 'When fooid = 4,foosubid=%,fooname=%', rec_emp.foosubid, rec_emp.fooname;
  END LOOP;
  
  -- Close the cursor
  CLOSE cur_emp;
END $$;




