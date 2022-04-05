-- mac下安装postgres
brew install postgresql@14

-- 查看版本,确认已安装
pg_ctl -V

-- 初始化数据库
/*
指定的数据目录(linux下的$PGDATA):-D,此选项指定应该存储数据库集群的目录,必传.也可以设置环境变量PGDATA来替换-D选项.
指定超级用户:-U,默认为运行initdb的电脑用户的名称.
指定字符集: -E UTF8,选择模板数据库的编码,这也是稍后创建任何数据库的默认编码
指定字符排序:--lc-collate=C
指定字符分类:--lc-ctype=en_US.UTF-8
指定消息语言:--lc-messages=en_US.UTF-8
其中与中文输入关系最密切的就是 LC_CTYPE,LC_CTYPE 规定了系统内有效的字符以及这些字符的分类,诸如什么是大写字母,小写字母,大小写转换,标点符号、可打印字符和其他的字符属性等方面。
而locale定义zh_CN中最最重要的一项就是定义了汉字(Class “hanzi”)这一个大类,当然也是用Unicode描述的,这就让中文字符在Linux系统中成为合法的有效字符,而且不论它们是用什么字符集编码的。
*/
initdb -D /Users/mt/other/postgresql -U mt --lc-collate=C --lc-ctype=en_US.UTF-8 --lc-messages=en_US.UTF-8 -E UTF8

-- 启动数据库
pg_ctl -D /Users/mt/other/postgresql  start

-- 生成默认数据库postgres与模板数据库template0,template1
createdb

-- 执行完以上所有操作后才可以在终端使用psql命令

-- 关于模板数据库template0与template1
/*
首先要牢记,后续所有create database db_name [template][template_name]建库都是默认基于模板库template1创建的,而template1的设置基于初始化initdb

template0与template1共同点是都不能被删除。

template0与template1的区别:
1.template1可以被连接并能创建对象(表,视图,函数等),而且当template1中创建对象后,后续新建的基于template1的database也会含有这些对象数据,而template0不能被连接,也就不能在
其中创建对象了,template1的优点是有些复用数据或插件在template1中创建后,新建的基于template1的database不必再去重复创建。

2.基于template0创建的database可以重新指定新的encoding,Collate,Ctype,当有些插件或场景需要重新指定这些设置来建库时,可以基于template1来创建,而不必去重新initdb初始化,相
反template1不支持重新指定这些编码。
*/

-- 除系统默认模板库外,新建模板库的2种方法
/*查看database属性,其中2个属性特别重要:datistemplate指定是否为模板库,datallowconn指定库是否可以被连接,template0不可连接,就是因为其datallowconn属性为f*/
select * from pg_database;

1.在创建时利用指定 is_template true
create database my_template is_template true;

2.将系统表pg_database中将需要修改为模板库的database的datistemplate的datistemplate属性修改为t,以下2种写法都行

alter database my_template is_template true;

update pg_database set datistemplate = 't' where datname = 'my_template';

-- 删除自定义的模板库,默认的模板库当然也可以删除,但正常人都不会去删吧？

1.先取消模板资格
alter database my_template is_template false;
update pg_database set datistemplate = 'f' where datname = 'my_template';

2.然后删除
drop database my_template;


