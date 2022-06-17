-- 1.嵌套子块
/*
do是执行的意思，$$标识一个过程块，do $$表示执行一个没有名字即匿名块
<<outer_block>> 声明这是一个嵌套块的外块,end outer_block标识外块结束
DECLARE 声明变量
赋值语法为 :=
%占位符
EGIN 和 END 之间是代码主体，所有的语句都使用分号结束
*/

DO 
$$ 
	<< outer_block >> 
DECLARE 
	name text;
BEGIN 
	name := 'outer_block';
	RAISE NOTICE 'This is %',name;
	DECLARE 
		name text := 'sub_block';
		BEGIN 
			RAISE NOTICE 'This is %',name;
			RAISE NOTICE 'The name from the outer block is %',outer_block.name;
		END;
	RAISE NOTICE 'This is %',name;
END 
	outer_block 
$$;



-- 2.基于表的行，基于表的字段，基于其他变量来定义变量
/*
myrow 是一个行类型的变量，可以存储查询语句返回的数据行（数据行的结构要和 tablename 相同）
y应当是一个已定义数据类型的变量，然后x与y类型一致

myrow   tablename%ROWTYPE;
myfield tablename.columnname%TYPE;
x       y%TYPE;

*/

CREATE TABLE foo (fooid INT, foosubid INT, fooname TEXT);  
INSERT INTO foo VALUES (1, 2, 'three');  
INSERT INTO foo VALUES (4, 5, 'six');  
  
CREATE OR REPLACE FUNCTION get_all_foo() RETURNS SETOF foo AS  
$BODY$  
DECLARE  
    r foo%rowtype;  
BEGIN  
    FOR r IN  
        SELECT * FROM foo WHERE fooid > 0  
    LOOP  
        -- can do some processing here  
        RETURN NEXT r; -- return current row of SELECT  
    END LOOP;  
    RETURN;  
END  
$BODY$  
LANGUAGE plpgsql;  
  
SELECT * FROM get_all_foo();


-- 3.记录类型变量
/*
记录类型的变量没有预定义的结构
只有当变量被赋值时才确定
可以在运行时被改变
*/
x RECORD;

do                                           
$$                                                                                          
declare x record;                                                                           
begin                                 
for x in SELECT * from foo loop    
RAISE NOTICE 'x.fooid=%,x.foosubid=%,x.name=%',x.fooid,x.foosubid,x.fooname;
end loop;                             
end;                                  
$$;   


-- 4.常量
/*
常量可以用于避免魔数（magic number），提高代码的可读性；
也可以减少代码的维护工作，所有使用常量的代码都会随着常量值的修改而同步，不需要修改多个硬编码的数据值
*/
PI CONSTANT NUMERIC := 3.14159265;


-- 5.returning x into y 把x赋值给y

create table test(id int,start_num int,end_num int);

do                                           
$$                                                                                          
declare x int :=0;                                                                           
begin                                 
for i in 1..10 loop    
-- 把第前一行的end_num赋值给中间变量x，在下一行中把x赋值给start_num
insert into test values(i,x,x+(random()*10)::int) returning end_num into x;
end loop;                             
end;                                  
$$;   

SELECT * FROM test


-- 6.VARIADIC 可变类型
/*
需要把数组也声明为可变
把数组爆炸，取出下标所对应的值,再min聚合
*/
- SELECT (ARRAY[3,1,4,2])[i] FROM generate_subscripts(ARRAY[3,1,4,2], 1) g(i);

CREATE FUNCTION mleast(VARIADIC numeric[]) RETURNS numeric AS $$
    SELECT min($1[i]) FROM generate_subscripts($1, 1) g(i);
$$ LANGUAGE SQL;

- SELECT mleast(10, 4, 5, 2); 返回 2
- SELECT mleast(3, 1, 2);返回1




























