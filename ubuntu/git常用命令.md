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

#### 从远程仓库拉取项目
1. 新建本地目录并切换进入
```sh
mkdir git_pull_test
cd git_pull_test
```
2. 在远程仓库中点击克隆/下载,获取远程仓库项目https地址
```sh
https://gitee.com/mangti/git_test.git
```
4. 拉取项目
```sh
// 注意:上文中gt别名拉取报错了
git clone https://gitee.com/mangti/git_test.git
```
5. 验证:成功
6. 记得在管理中修改仓库开源

#### git流程逻辑整理
1. 4个空间

|空间|功能|状态|后续操作|备注|
|---|---|---|---|---|
|工作区|本地项目文件夹|untracked,unstage未追踪|将需要的文件add进暂存区|记得先git init初始化目录|
|暂存区|暂存准备commit的文件|stage已追踪|将整个暂存区commit到本地版本库|使用-m来备注版本说明,默认使用vim编辑版本说明|
|本地版本库|暂存commit提交的文件|是否有commit的内容|将本地版本库推送至远程仓库|---|
|远程仓库|统一存放最新版本的代码文件|---|clone最新版本到工作区,根据远程仓库直接更新整个工作区|如果误选择工作区影响比较大|
|---|---|---|fetch更新到本地版本库,diff对比工作区文件|对比确认无误后再更新至工作区|

2.实操示例
- 基本操作
```sh
// 新建本地工作区
mkdir git_dir

// 切换至本地工作区
cd git_dir

// 配置用户及email
git config --global user.name "your name"
git config --global user.email your_email@xx.com

// 初始化目录,表明该目录需要进行版本控制
// 会自动创建隐藏文件.git(mac下查看隐藏文件shift+command+.),另外初始化后终端会显示master主分支
git init

// 创建一个test.txt文件,并写入内容:'版本1'
// echo与touch区别:touch只创建文件,echo可以在创建文件的同时写入内容
echo "版本1" > test.txt

// 查看git状态,会返回当前所在分支,是否需要commit,被跟踪的文件,未被跟踪的文件
git status

// 将test.txt添加至暂存区
git add test.txt

// 再次查看git状态
git status

// 提交暂存区的文件至本地版本库,注意这里的版本1是版本说明而非txt中的内容版本1
// 使用-m进行简短的版本说明,如果版本说明较长则不加-m参数,进入默认的vim编辑器中编辑版本说明
git commit -m '版本1'

// 第三次查看git状态,此时会显示所有文件已提交
git status

// 特殊操作,使用文本编辑器在test.txt中新增一行内容:'版本2',并添加至暂存区
git add test.txt

// 继续使用文本编辑器在test.txt中新增一行内容:'版本3',但不进行add,此时查看git状态
git status
// 发现存在一个待提交的test.txt(写入内容:版本2)和一个未追踪的test.txt(写入内容:版本3)

// 再次添加至暂存区,暂存区中待提交的test.txt会被更新(写入内容包含版本2和版本3)
git add test.txt

// 将暂存区内容再次commit提交到本地版本库
git commit -m "版本2和版本3"

// 查看历史版本,会出现2个版本,分别为:版本1/版本2和版本3
// log中除了展示版本说明还展示了commit hash串,作者和提交时间
// q退出log
git log


// 新建test1.md文件写入:我不想被提交至本地版本库
echo "我不想被提交至本地版本库" > test1.md

// 查看git状态,可以看到test1.md的状态
git status

// 创建.gitignore隐藏文件并写入test1.md,即可忽略追踪test1.md的状态
// .gitignore应在工作区根目录下
// 注意:被忽略跟踪的文件在其他分支中如果被删除,主分支也会受影响
echo "test1.md" > .gitignore

```
- 分支逻辑
```sh
// 以上master主分支中存在2个版本,版本1/版本2和版本3
// 现在有个聪明人觉得这2个版本都不好,想自己增加部分内容,但不确定是否能开发成功或被采用
// 此时即可创建一个分支git branch+分支名
git branch bad-boy

// 查看有哪些分支,q退出,与git config一样,带参数则是新建或修改,不带参数则是查看
git branch

// 切换至分支git checkout+分支名,切换成功后终端会显示分支名
git checkout bad-boy

// 删除文件夹中test.txt与test1.md文件,然后add并commit连写直接从工作区提交至本地版本库
git commit -a -m "刚刚删除了2个文件"

// 切换回master分支,检查bad-boy分支删除文件对主分支的影响
// test.txt还在主分支的文件夹,但是test1.md被删除了,因为test1.md被忽略跟踪所导致的
git checkout master

// 删除bad-boy分支,git branch -d 分支名
// 提示分支尚未被合并,如果确定删除请使用-D
git branch -d bod-boy
git branch -D bod-boy

// 创建新分支temp并切换至temp新分支的简写
git checkout -b temp

// 使用文本编辑器在temp分支中test.txt副本里添加内容:'版本4'
// 将分支副本test.txt提交至本地版本库
// 参数也可以继续简写做-am
git commit -a -m "版本4"

// 合并分支,git merge + 分支名,应当在主分支中合并其他分支,所以在合并分支前应先切换至主分支
// 合并后主分支test.txt中已有内容:'版本4'
// 注意分支内容冲突,比如将其中一个分支的副本内容中的版本1改成版本一,请手动修改2个分支一致
git checkout mastrt
git merge temp
```
- 远程仓库配置
```sh
// 新建仓库并新建test.txt文件写入:'版本1'
// 从远程仓库拉取到本地工作区,点击code,复制clone中的https远程仓库地址xxx.git,回到本地文件夹
git clone xxx.git

// 注意远程仓库的主分支叫main,本地主分支叫master

// 在clone下来的副本test.text中新增一行内容:'版本2',并提交至本地版本库
git commit -am '版本2'

// 查看本地仓库与那些远程仓库有联系,其中返回的origin是别名,便于使用origin代替长长的仓库地址
git remote -v

// 推送到远程仓库,github2021年不支持用户名和密码来push代码了,需要先获取token
// 在github点击头像settings中进入developer settings打开personal access tokens点击generate new token生成新token配置token名与权限
git push
username:xxx
token:xxx     // 与密码一样,token默认不显示,粘贴获取到的token后回车即可

// 在远程仓库test.txt中继续新增一行内容:'版本3'后回到本地
// 将远程仓库更新先暂存到本地版本库
git fetch

// 对比本地版本库与工作区文件,git diff 远程仓库名/分支名
git diff origin/main

// 从本地版本库拉取到工作区
git pull

// 查看历史版本
git log

```

- vscode中的git
```sh
// 打开目录
// 打开版本控制功能(debug功能图标上方)
// 初始化git目录,其中U表示未追踪,点击U,点击+号,更新为A表示被添加至暂存区
// message框输入版本说明,点击上方√完成commit提交
// 分支创建合并等功能在...中,分支切换点击左下角当前分支
```

#### 实践
- 在gitee上创建仓库pc_work,获取https远程地址
```sh
https://gitee.com/mangti/pc_work.git
```
- 创建本地工作区并push至gitee仓库
```sh
mkdir pc_work
cd pc_work
echo "## readme" > readme.md
git init
git branch master
git checkout master  
git commit -a -m '测试1'
git status
git remote add gitee https://gitee.com/mangti/pc_work.git
git remote -v
git push gitee
```
- 在gitee上给readme新增内容:测试2,pull到本地
```sh
// 注意远程仓库与分支的连接方式,diff需要比较具体分支所以是/
git fetch gitee master
git diff gitee/master
git pull gitee master
git log
```











































