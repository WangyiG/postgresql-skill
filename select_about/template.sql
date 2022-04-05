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

-- 生成默认数据库postgres与模版数据库template0,template1
createdb

-- 执行完以上所有操作后才可以在终端使用psql命令

-- 关于模版数据库template0与template1
/*
1.首先要牢记,后续所有create database db_name [template][template_name]建库都是默认基于模版库template1创建的,而template1的设置基于初始化initdb
2.template0与template1的区别:
template0不能被连接,template1可以被连接并创建对象(表,视图,函数等),并�且
*/
