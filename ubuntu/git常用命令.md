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












































