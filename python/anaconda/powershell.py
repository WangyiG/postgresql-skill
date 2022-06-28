# D:\Python\anaconda\Scripts 把Scripts目录路径添加至系统变量
conda init powershell

// 查看当前虚拟环境列表
conda env list

// 创建虚拟环境
sudo conda create -n drf python=3.8

// 切换活跃环境
conda activate drf

conda deactivate drf

// 删除指定虚拟环境
conda remove -n drf --all
