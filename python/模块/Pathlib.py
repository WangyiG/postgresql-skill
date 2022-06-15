from pathlib import *

input_path = r"C:\Users\wangy\Documents\pandas学习\VScode\excel\be.a_b.xls"

# 路径处理信息提取

## 文件名+后缀,返回类型为str
Path(input_path).name

## 不带最后一个后缀的文件名或文件夹最后一级目录,返回类型为str
Path(input_path).stem,Path(input_path).parent.stem

## 最后一个后缀,返回类型为str
Path(input_path).suffix

## 多个.的文件视为多个后缀
Path(input_path).suffixes

## 返回父级目录,返回类型为Path对象
Path(input_path).parent

## parents切片取向上第几个的父级目录
Path(input_path).parents[1]

## 返回该路径上所有节点的一个tuple,同样支持切片取
Path(input_path).parts,Path(input_path).parts[2:4]



# 路径判断

input_path2 = r'C:\Users\wangy\Documents\abc\VScode\excel'

if Path(input_path2).exists():
    if Path(input_path2).is_dir():
        print(f'{Path(input_path2).stem} 是文件夹.')
    elif Path(input_path2).is_file():
        print(f'{Path(input_path2).stem} 是文件.')
else:
    print(f'{Path(input_path2).resolve()} 不存在,请仔细检查路径.')
    

# 目录拼接

## 1.Path与方法接收2个参数,第一个参数可为path对象也可为字符串
Path(Path(input_path).home(),Path('D:','test')    

## 2.Path.joinpath方法，第一个参数必须为path对象
Path.joinpath(Path(input_path).home(),'test')

## 3.语法糖,path对象使用/连接符来拼接
Path(input_path).home()/'test'/'t.xls'


 
# 路径建立与删除
     
## 创建文件夹,文件夹存在会报错,所以要先exists判断，更新mkdir有参数exist_ok=True，实现存在则忽略，否则创建
#  创建文件则是Path.touch()
     
new_dir = Path(r"C:\Users\wangy\Documents\pandas学习\VScode\test")
if not new_dir.exists():
    new_dir.mkdir()
     
## 删除文件夹，文件夹为空才能删除，否则也会报错
     
new_dir.rmdir()
     
## 删除文件
     
old_file = Path(r"C:\Users\wangy\Documents\pandas学习\VScode\emm\a.txt")
old_file.unlink()
     

     
# 路径迭代查找
     
path_ = Path(r'C:\Users\wangy\Documents\pandas学习\VScode\emm')
     
     
##  iterdir返回类型是一个生成器，查找当前路径下的文件夹与文件，不会深入子文件夹
     
list(path_.iterdir())
    
## glob(pattern)返回类型是一个生成器，查找当前路径下所有与 pattern 匹配的文件，不会深入子文件夹   
     
list(path_.glob('*.txt'))
     
## rglob(pattern)返回类型是一个生成器，查找当前路径及子文件夹下所有与 pattern 匹配的文件，深入子文件夹

list(path_.rglob('*.txt'))
     


# 读写文件
# w模式下文件不存在会先创建文件,这里需要注意的是只有最后的文件不存在会创建，如果上一层文件夹也不存在,则必须要先mkdir创建文件夹

 with (path_/'over.txt').open('w') as fw:
    fw.write('Over!')    
     
     
# 一个简单示例
# 将excel文件夹中的xls文件转成csv存入excel同级的csv文件夹

input_path = r"C:\Users\wangy\Documents\pandas学习\VScode\excel\ae.xls"

# 先创建dir
dir = Path(input_path).parents[1]/'csv'
if not dir.exists():
    dir.mkdir()

# 然后才能用dir路径
pd.read_excel(input_path).to_csv(dir/(Path(input_path).stem+'.csv'),index=False)
 
     
   
     
     
