 -- install
 brew install postgresql@14 

 -- 查看版本,确认已安装
 pg_ctl -V
 
 -- 初始化数据库,mt为实际的电脑用户名
 initdb -D /Users/mt/other/postgresql -U mt --lc-collate=C --lc-ctype=en_US.UTF-8 --lc-messages=en_US.UTF-8 -E UTF8 
 
 -- 如果是重新安装，初始化提示，之前文件夹已存在，需要重建路径或先删除原路径
 rm -rf /Users/mt/other/postgresql
 
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
