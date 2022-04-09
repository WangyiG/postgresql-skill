impor numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 数据准备
arr = np.arange(25).reshape(5,-1)
brr = np.vstack((arr,arr.T))
m2 = np.vstack((brr[:,:2],brr[:,1:3],brr[:,2:4],brr[:,3:5])) 
df = pd.DataFrame(m2,columns=['a','b'])


G = nx.from_pandas_edgelist(df,source='a',target='b')

# 设置图的布局,布局有很多,可以去文档翻翻
pos = nx.kamada_kawai_layout(G)

# 图像细节设置
nx.draw(G,pos,with_labels=True,node_color=range(25),node_size=400,edge_color=range(df.shape[0]),width=1,alpha=0.6,
        arrowstyle="->",arrowsize=10,font_size=14, font_family="sans-serif")

#nx.draw(G,pos,with_labels=True)
plt.show()

# 所需起点至终点路径,路程设置为8,是为了筛出向右向下走法,对于5*5矩阵起点到终点路程一定是8
list(nx.all_simple_paths(G,0,24,cutoff=8))[:10],len(list(nx.all_simple_paths(G,0,24,cutoff=8)))

# 动态规划求最小路径和
def min_sum(arr):
    m,n= arr.shape[0],arr.shape[1]
    dp = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if i==j==0:
                dp[i][j] = 0
            elif i==0:
                dp[i][j] = dp[i][j-1]+arr[i][j]
            elif j==0:
                dp[i][j] = dp[i-1][j]+arr[i][j]
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+arr[i][j]
    return dp

min_sum(arr)



