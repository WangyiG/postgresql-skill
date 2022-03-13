/*匿名块可以视为一个无须创建即可执行的函数,注意其返回值是void类型，
是一种抽象类型，不可直接定义变量，但可执行create,insert into等操作
注意declare声明多个参数时竟然是用;分隔的，逗号分隔出错了，不科学
*/

-- 1.一个最简单的do匿名块

-- 创建一个test表
create table test(id int,start_num int,end_num int);

/*指定使用的语言是plpgsql，还可使用其他如c，python等语言*/
do language plpgsql                   
/*双$$标识符包裹住函数体，并可在中间填写函数用途，前后必须一致*/                                             
$do_test$                                                                                          
declare x int :=0;                                                                           
begin                                 
for i in 1..10 loop                   
insert into test values(i,x,x+(random()*10)::int) returning end_num into x;
end loop;                             
end;                                  
$do_test$;   
 
/* 
do language xx       看做do函数头
$$                   do函数标识层起始                        
declare xx;          参数声明: 变量 变量类型 :=（赋值符号） 初始值
begin                do函数body层起始
for xxx loop         循环起始

# 空行隔开这一段通常由do函数头指定的语言编写，不妨叫它语言层
示例中returning end_unm into x意为把x由初始值重新赋值为end_num

end loop；           循环结束
end；                do函数body层结束
$$；                 do函数标识层结束
*/

-- 2.do匿名块中简单的分支示例

-- 2(1).if
do $$ 
declare x int := 3;
begin

if x=2 THEN 
create table a(id int);
else 
drop table a;
end if;

end;
$$ language plpgsql;

-- 2(2).case when
do language plpgsql $$ 
declare x boolean := false;
begin

case when x THEN 
create table a(id int);
ELSE 
drop table a;
END case;

end;
$$;

-- 3.do匿名函数中简单的循环示例，注意其中declare多个参数时用的;分隔,for loop在1中已演示，这里演示另外2种

-- 3(1).loop  exit when xxx  end loop
create table test(id int);

do language plpgsql $$
declare
 
m int:=0;
n int:=5;

begin

loop

insert into test values(m+1) returning id into m;
exit when m=n;

end loop;

end;
$$;

-- 3(2).while xxx loop   end loop
create table test(id int);

do $$
declare m int:=0;n int:=5;
begin

while m<=n loop
insert into test values(m+1) returning id into m;
end loop;

end;
$$ language plpgsql;

