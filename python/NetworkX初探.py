import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 数据准备
d,f = pd.read_excel('/Users/mt/Desktop/求每个节点的最短路径.xlsx',None).values()
df = pd.concat([d,f])

# 根据df生成有向图,step列为有向边的起点，step_previous为有向边的终点,edge_attr='weights'权重这里省略
# create_using=nx.DiGraph()参数指定有向
G = nx.from_pandas_edgelist(df,source='Step',target='Step_Previous')

# 设置布局,调整图像不要纠缠太混乱
pos = nx.kamada_kawai_layout(G)

# 做图
nx.draw(G,pos,with_labels=True,node_color=range(42),node_size=400,edge_color=range(df.shape[0]),width=1,alpha=0.6,
        arrowstyle="->",arrowsize=10,font_size=14, font_family="sans-serif")

nx.draw(G,pos,with_labels=True)
plt.show()

# 标识边的长度示例
df = pd.DataFrame({'begin':list('AABC'),'end':list("BCAB"),'length':[1,3,5,7]})
G = nx.from_pandas_edgelist(df,source='begin',target='end',edge_attr='length')
pos=nx.spring_layout(G);
nx.draw(G, with_labels=True,edge_color='black')
nx.draw_networkx_edge_labels(G,pos,font_color='r',edge_labels= nx.get_edge_attributes(G, 'length'),rotate=True)
plt.show()

‘’‘
1.https://blog.csdn.net/qq_40206371/article/details/118061345
2.https://blog.csdn.net/littlely_ll/article/details/81749960
3.https://www.osgeo.cn/networkx/reference/drawing.html#module-networkx.drawing.nx_agraph
’‘’
