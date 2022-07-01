## apt-get
apt-get是一个deb包的管理工具
常用参数与常用命令:
- 参数
```sh
// 默认同意
apt -y 
```
- 升级与安装
```sh
apt-get update						        ah           // 更新源文件，并不会做任何安装升级操作
apt-get upgrade						                   // 系统与软件更新
apt-get install packagename				           // 安装指定的包
apt-get install packagename --only-upgrade	 // 仅升级指定的包
apt-get install packagename --reinstall   	 // 重新安装包
apt-get -f install   					               // 修复安装
apt-get build-dep packagename				         // 安装相关的编译环境
apt-get source packagename  				         // 下载该包的源代码
apt-get dist-upgrade 					               // 升级系统
apt-get dselect-upgrade 				             // 使用 dselect 升级
```
- 查询与显示
```sh
apt-cache search packagename 				  // 查询指定的包  　　
apt-cache show packagename 				    // 显示包的相关信息，如说明、大小、版本等 
apt-cache depends packagename 				// 了解使用该包依赖哪些包
apt-cache rdepends packagename 				// 查看该包被哪些包依赖
```
- 删除与检查清理
```sh
apt-get remove packagename				          // 删除包  　　
apt-get remove packagename -- purge 			  // 删除包，包括删除配置文件等 
apt-get autoremove packagename --purge 			// 删除包及其依赖的软件包+配置文件等（只对6.10有效，推荐使用）
apt-get clean 						                  // 清理无用的包 
apt-get autoclean 					                // 清理无用的包 
apt-get check 						                  // 检查是否有损坏的依赖
```

## 查看ubuntu系统是64位还是32位
sudo uname --m

## 更新
```sh
sudo apt update
sudo apt -y upgrade
```
## 重启系统
```sh
sudo reboot
```

## 我的mac上安装conda
- wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2022.05-Linux-aarch64.sh
- bash Anaconda3-2022.05-Linux-aarch64.sh
- 注意安装过程中有1步conda init 要yes，配置环境变量
- source ～/.bashrc

## 安装postgre
默认用户是postgres
```sh
// 查看当前包列表
apt show postgresql
// 创建文件存储库配置
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
// 导入存储库签名密钥
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
#更新包列表
sudo apt update
// 安装最新版本的PostgreSQL。
// 如果需要特定版本，请使用“postgresql-14”或类似版本，而不是“postgresql”：
sudo apt -y install postgresql-14
// 检查版本
psql --version
```

## 安装nodejs
```sh
// 指定安装源
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
// 默认同意安装
sudo apt-get install -y nodejs
检查版本
node -v 
npm -v
```

