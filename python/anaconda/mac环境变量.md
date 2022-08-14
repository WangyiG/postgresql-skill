##进入配置
```sh
// i编辑模式,esc退出编辑模式,:wq写入保存并退出
vim ~/.zshrc
```
## 加载配置
```sh
source ~/.zshrc
```
#### miniforge卸载重装
- 官网
```sh
https://github.com/conda-forge/miniforge
```
- 卸载
```sh
conda init --reverse --dry-run
conda init --reverse

CONDA_BASE_ENVIRONMENT=$(conda info --base)
echo The next command will delete all files in ${CONDA_BASE_ENVIRONMENT}
rm -rf ${CONDA_BASE_ENVIRONMENT}

echo ${HOME}/.condarc will be removed if it exists
rm -f "${HOME}/.condarc"
// 检查mt用户文件夹下miniforge文件夹是否还存在,可手动删除

// 如果是brew安装的则brew uninstall miniforge
```
- 重装
```sh
brew install --cask miniforge
conda init "$(basename "${SHELL}")"
// 安装目录为
/opt/homebrew/bin/conda
```
#### vscode中使用jupyter
```sh
conda install jupyter
```
#### 常用虚拟环境配置
- dash
```sh
conda create -n dash_dev python=3.8 -c https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/main/ -y
conda activate dash_dev
pip install dash feffery-antd-components arrow pandas  -i https://pypi.douban.com/simple/
pip install peewee -i https://pypi.douban.com/simple/
// postgresql需要安装
conda install psycopg2 
```
- geopandas
```sh
conda create -n geopandas-env python=3.8 -c https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/main -y
conda activate geopandas-env
conda install pandas jupyter geopandas=0.11.0 pyogrio pygeos -c https://mirrors.sjtug.sjtu.edu.cn/anaconda/cloud/conda-forge -y
conda install matplotlib
conda install -c conda-forge ipympl
```







