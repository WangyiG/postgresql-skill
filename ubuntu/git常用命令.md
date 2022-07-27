#### git常用命令
- 查看某个命令的帮助
```sh
git help <command>
git <command> -h
git <command> --help
```
- 用户配置
```sh
// --global影响当前用户的所有仓库
// --system影响全系统的git仓库
git config --global user.name "bettyaner"
git config --global user.email bettyaner@163.com

// 查看git配置信息
git config --list

// git用户名、密码、邮箱的配置(重新配置即是修改,不带xxx即是查看)
git config user.name  xxx
git config user.password  xxx
git config user.email   xxx
```
- 常用命令
```sh
// 初始化仓库,生成隐藏的.git目录
git init 

// 跟踪内容状态和文件状态
// 内容状态标示内容文件的改变，有三个区域：工作目录，暂存区和提交区
// 文件状态有两个状态：已跟踪和未跟踪
git status

// 添加文件内容到暂存区（同时文件被跟踪）
	git add
	
// 添加所有文件
git add . 或  git add -A

// 并不是所有文件都想被跟踪，可以配置.gitignore配置忽略文件
git rm --cached :仅从暂存区删除
git rm :从暂存区与工作目录同时删除
git rm $(git ls-files --deleted):删除所有被跟踪，但是在工作目录被删除的文件

// 提交
git -commit -m 'first commit' //从暂存区提交 -m：注释
git commit -a -m 'full commit'从工作区提交

//查看提交历史记录
git log 

//将文件内容从暂存区复制到工作目录
git checkout -- <file> 

// git push <远程主机名> <本地分支名>:<远程分支名>,-f表示强制推送
git push -f https://gitee.com/mangti/docs.git master:gh-pages

// git pull <远程主机名> <远程分支名>:<本地分支名>,-f表示强制拉取
```
#### gitee
- 创建测试目录结构如下
```sh
gittest
├── app1
│   ├── a1.txt
│   ├── b1.txt
│   ├── c1.txt
│   └── migrations
│       ├── __init__.py
│       ├── a1.py
│       └── b1.py
├── app2
│   ├── a2.txt
│   ├── b2.txt
│   ├── c2.txt
│   └── migrations
│       ├── __init__.py
│       ├── a2.py
│       └── b2.py
└── app3
    ├── a3.txt
    ├── b3.txt
    ├── c3.txt
    └── migrations
        ├── __init__.py
        ├── a3.py
        └── b3.py
```
- 在自己的gitee账户中创建远程仓库
```md
1. 配置仓库名称,尽量与项目一致,并对仓库进行描述
2. 配置路径,一般根据仓库名称自动生成
3. 配置仓库私有还是开源,20220727日开源好像得先配置私有,仓库创建之后再修改为公开
4. 其余按默认设置
```
#### 将本地项目推送到远程仓库
```md
1. 在项目根目录下配置.gitignore文件配置忽略推送
```sh
# mac下shift+command+.查看隐藏文件

# 忽略所有app下migrations中的非init文件
*/migrations/*.py
!*/migrations/__init__.py

# 写要忽略的部分,如下则a开头的只有a3,b开头的只有b1
a[12].txt
B[23].txt
```
```
2. 本地操作:init初始化项目,add将项目文件添加至暂存区,commit提交(-m:提交注释)
```sh
// 项目根目录下
git init
git add .
git commit -m 'first commit'
```
3. 推送:push 远程仓库https+分支
```sh
// 给远程仓库地址(gitee新建仓库中给出的https地址)创建别名为gt
git remote add gt https://gitee.com/mangti/git_test.git
// 推送到别名为gt的地址+分支
git push gt master
```
4. 反馈
```sh
// 刷新远程仓库发现.gitignore生效了,需要注意的应该在其中继续忽略.DS_Store(mac系统生成的隐藏文件)
```
```

#### 从远程仓库拉取项目
```md
1. 新建本地目录并切换进入
```sh
mkdir git_pull_test
cd git_pull_test
```
2. 在远程仓库中点击克隆/下载,得到https地址
```sh
https://gitee.com/mangti/git_test.git
```
4. 拉取项目
```sh
// 注意:上文中gt别名拉取报错了
git clone https://gitee.com/mangti/git_test.git
```
5. 验证:成功
```











































