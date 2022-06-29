# D:\Python\anaconda\Scripts 把Scripts目录路径添加至系统变量
conda init powershell

// 查看当前虚拟环境列表
conda env list
conda info -e

// 创建虚拟环境
sudo conda create -n drf python=3.8

// 切换活跃环境
conda activate drf

conda deactivate drf

// 删除指定虚拟环境
sudo conda remove -n drf --all

// 查看当前环境中手动安装的包
pip freeze

// 查看手动安装的包以及当前环境中运行的依赖
pip list

// 打包
pip freeze > ./requirements.txt
切换至txt所在目录,pip install -r requirements.txt


// 镜像源
// 查看当前源
conda config --show-sources

// 新增源
conda config --add channels https://pypi.douban.com/anaconda/cloud/conda-forge/
  
// 删除所有源  
conda config --remove-key channels
