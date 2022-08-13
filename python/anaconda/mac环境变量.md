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
