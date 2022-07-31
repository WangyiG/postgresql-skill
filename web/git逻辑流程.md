# git逻辑流程

## 常用命令
#### 1.新建并切换至本地工作区文件夹
```sh
mkdir git_dir
cd git_dir
```
#### 2.配置git全局用户
```sh
git config --global user.name "your name"
git config --global user.email your_email@xx.com
```

#### 3.初始化目录,表明该目录需要进行版本控制
- 该命令会自动创建隐藏文件.git
- mac下查看隐藏文件shift+command+.
- 初始化后终端一般显示master主分支
```sh
git init
```

#### 4.创建一个test.txt文件,并写入内容:'word1'
- touch只创建文件,echo可以在创建文件的同时写入内容
```sh
echo "word1" > test.txt
```

#### 5.查看git状态
- 返回当前所在分支
- 返回有无需要commit
- 返回被跟踪的文件,未被跟踪的文件
```sh
git status
```

#### 6.将test.txt添加至暂存区
- 注意 add . 与 add —A 的区别
```sh
git add test.txt
```

#### 7.提交暂存区的文件至本地版本库
- 使用-m进行简短的版本说明,如果版本说明较长则不加-m参数,进入默认的vim编辑器中编辑版本说明
- 文件添加至暂存区的操作可以以-a参数合并执行,git commit -am '###'
```sh
git commit -m '版本1'
```

#### 8.查看历史版本
```sh
// 使用文本编辑器在test.txt中新增一行内容:'word2',并添加至暂存区
git add test.txt

// 继续使用文本编辑器在test.txt中新增一行内容:'word3',但不进行add,此时查看git状态
git status
// 发现存在一个待提交的test.txt(写入内容:word2)和一个未追踪的test.txt(写入内容:word3)

// 再次执行添加至暂存区操作,test.txt会被更新(最新内容包含word2和word3)
git add test.txt

// 将暂存区内容再次commit提交到本地版本库
git commit -m "版本2"

// 查看历史版本,会出现2个版本,分别为:版本1/版本2
// log中除了展示版本说明还展示了commit hash串,作者和提交时间
// q退出log
git log
```

#### 9..gitignore文件
- 被该文件中写入的内容所匹配的文件将被忽略追踪
- 缺点:因为被忽略跟踪的原因,被忽略的文件如果在其他分支中被删除,主分支也会受影响
```sh
// 新建test1.md文件写入:我不想被提交至本地版本库
echo "我不想被提交至本地版本库" > test1.md


// 创建.gitignore隐藏文件并写入test1.md,即可忽略追踪test1.md的状态
echo "test1.md" > .gitignore

```


## git分支
#### 1.git branch 分支
- 创建的新分支会以主分支创建副本
- 与git config类似,带分支名则是新建或修改,不带则是查看分支信息
- 与git log类似,q退出查看
```sh
// 以上master主分支中存在2个版本,版本1/版本2
// 现在有个聪明人觉得这2个版本都不好,想自己增加部分内容,但不确定是否能开发成功或被采用
// 此时即可创建一个分支
git branch bad-boy

// 查看有哪些分支,q退出
git branch
```
#### 2.git checkout 分支
- 通过 -b 参数合并执行分支创建与切换, git checkout -b 分支名
- 通过 -d 与 - D 参数删除分支,-D更加强力无需确认,git branch -D 分支名
```sh
// 切换至bad-boy分支,切换成功后终端会显示bad-boy分支名
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
```

#### 3.git merge 分支
- 应当在主分支中合并其他分支,所以在合并分支前应先切换至主分支
```sh
// 创建新分支temp并切换至temp新分支的简写
git checkout -b temp

// 使用文本编辑器在temp分支中test.txt副本里添加内容:'word4'
// 将分支副本test.txt提交至本地版本库
// 参数也可以继续简写做-am
git commit -a -m "版本4"

// 注意分支内容冲突,比如将其中一个分支的副本内容中的版本1改成版本一,请手动修改2个分支一致
git checkout mastrt
git merge temp
```


## 远程仓库
#### 1.先在github中创建1个远程仓库git_test
- 创建一个readme.md以做测试
#### 2.给远程仓库地址设置别名
- 在远程仓库中点击clone,复制其中的https远程仓库地址xxx.git_test.git
- 一般git会默认设置一个别名origin
- git remote -v 查看本地仓库与那些远程仓库有联系
```sh
git remote add github xxx.git_test.git
```
#### 2.拉取至本地
- 在本地创建一个文件夹用于存放将要被拉取下来的git_test文件夹
- clone与pull,clone比较粗心需要我们细心一点,pull拉取步骤更清晰
- 注意github远程仓库的主分支叫main,而gitee主分支叫master与本地默认主分支名一致
```sh
mkdir xxx
cd xxx

// clone直接从远程仓库拉取到本地工作去
git clone github

// 先从远程仓库拉取到本地版本库
git fetch github master

// 对比本地版本库与工作区文件
git diff github/master

// 从本地版本库拉取到工作区
git pull github master
```
#### 3.推送到远程仓库
- 推送时有仓库地址还不够还需要进行验证
- github2021年起password验证的是token
- 在github点击头像settings中进入developer settings打开personal access tokens点击generate new token配置token名和权限生成新token
- 推送时也需要注意分支匹配
```sh
// 新建main分支方便与github主分支名main匹配
git checkout -b main

// 在clone下来的副本test.text中新增一行内容:'word_test',并提交至本地版本库
git commit -am 'test'

// 查看本地仓库与那些远程仓库有联系
git remote -v

// 进行推送
git push xxx.git_test.git main
username:xxx
password:xxx     // 与密码一样,token默认不显示,粘贴获取到的token后回车即可

```
---

::: info 4个空间

|空间|功能|状态|后续操作|备注|
|---|---|---|---|---|
|工作区|本地项目文件夹|untracked,unstage未追踪|将需要的文件add进暂存区|须先git init初始化|
|暂存区|暂存准备commit的文件|stage已追踪|将整个暂存区commit到本地版本库|使用-m来备注版本说明,默认使用vim编辑版本说明|
|本地版本库|暂存commit提交的文件|是否有commit的内容|将本地版本库推送至远程仓库|---|
|远程仓库|统一存放最新版本的代码文件|---|clone最新版本到工作区,根据远程仓库直接更新整个工作区|如果误选择工作区影响比较大|
|---|---|---|fetch更新到本地版本库,diff对比工作区文件|对比确认无误后再更新至工作区|

:::
