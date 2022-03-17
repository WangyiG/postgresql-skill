-- 1.最简单的自定义函数两数相加add
/*
语法如下，注意缩进关系以及分号的使用：
create or replace 
    function func_name(arg arg_type,..) returns return_type                       -- 创建函数并指定函数名，参数与参数类型，返回值类型
as                                                                                -- create xx as语句,create table as，create view as
$$                                                                                -- 函数体起始标记
    declare                                                                       -- 声明关键词:声明变量 变量类型 赋值(:=)为初始值0
        res res_type := 0;                                                        -- 声明多个变量,请记住是以;分隔，而不是以逗号分隔以;结尾 
    begin                                                                         -- 语句开始标记 
        xxx;                                                                      -- 具体语句
        return res;                                                               -- 返回语句
    end;                                                                          -- 语句结束标记 
$$;                                                                               -- 函数体结束标记
language plpgsql;                                                                 -- 指明具体语言，是C还是python等,该指定也可放在create as语句中,且指定在as前,如1(1) 

调用:select func_name(arg,..);
删除:drop function func_name;
*/

-- 1(1).确定的参数与参数数据类型

create or replace function 
    add(m int,n int) returns int 
language plpgsql  
as
$$
    declare 
        res int;
    begin
        res = m + n;
        return res;
    end;
$$;

-- 1(2).确定的参数数据类型,用$1..$n指代参数

create or replace 
    function add1(int,int) returns int 
as
$$
    declare 
        res int;
    begin
        res = $1+$2;
        return res;
    end;
$$ language plpgsql;

-- 1(3).在创建时不仅可以指定数据类型,还可以指定参数是输入(in)还是输出(out)类型,部分代替declare的作用

create or replace 
    function add2(m int,n int,res out int) returns int 
as
$$
    begin
        res = m+n;
    end;
$$ language plpgsql;


-- 2.自定义函数需要确定好returns的数据类型，有以下几种写法
/*
以下几种示例中均无需declare,也顺便省略了begin end层
*/

-- 2(1).在table中指定输出的数据类型是int与text,参数名res1与res2会做结果集的列名,不宜缺省

create function 
	dup(int) returns table(res1 int,res2 text)
as
$$
    select $1,cast($1 as text)||' is text';
$$ language sql;

-- 2(2).create type type_name as语句指定结果集数据类型,然后让returns根据type_name调用指定的数据类型

create type mytype as (res1 int,res2 text);

create function 
	dup1(int) returns mytype
as
$$
    select $1,cast($1 as text)||' is text';
$$ language sql;

-- 2(3).在函数定义中不仅指定数据类型,顺便指定输入输出类型,可以省去returns,大善

create function 
	dup2(in int,out res1 int,out res2 text) 
as
$$
    select $1,cast($1 as text)||' is text';
$$ language sql;

