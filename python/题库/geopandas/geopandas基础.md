## 安装配置
- 安装
```sh
conda create -n geopandas-env python=3.8 -c https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/main -y
conda activate geopandas-env
conda install geopandas=0.11.0 pyogrio pygeos -c https://mirrors.sjtug.sjtu.edu.cn/anaconda/cloud/conda-forge -y

// vscode可能需要升级ipykernel
conda install -n geopandas-env ipykernel --update-deps --force-reinstall
```
- 验证安装
```py
import geopandas as gpd
gpd.__version__
```
- 在jupyter中使用交互式绘图模式%jupyter widget
```sh
conda activate geopandas-env

// 安装ipympl扩展,参见https://blog.csdn.net/OtakuParadox/article/details/108992718
conda install -c conda-forge ipympl
```

