-- mac下安装postgres
brew install postgresql@14

-- 查看版本,确认已安装
 pg_ctl -V

-- 初始化数据库
/*
指定的数据目录:/Users/mt/other/postgresql
指定管理员:-U mt
指定字符集: -E UTF8
指定字符排序:--lc-collate=C
指定字符分类:--lc-ctype=en_US.UTF-8
指定消息语言:--lc-messages=en_US.UTF-8
其中与中文输入关系最密切的就是 LC_CTYPE,LC_CTYPE 规定了系统内有效的字符以及这些字符的分类,诸如什么是大写字母,小写字母,大小写转换,标点符号、可打印字符和其他的字符属性等方面。
而locale定义zh_CN中最最重要的一项就是定义了汉字(Class “hanzi”)这一个大类,当然也是用Unicode描述的,这就让中文字符在Linux系统中成为合法的有效字符,而且不论它们是用什么字符集编码的。
*/
initdb -D /Users/mt/other/postgresql -U mt --lc-collate=C --lc-ctype=en_US.UTF-8 --lc-messages=en_US.UTF-8 -E UTF8

-- 启动数据库
