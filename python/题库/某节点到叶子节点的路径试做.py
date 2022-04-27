import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 数据
df = pd.DataFrame([[1, 2],[1, 4],[2, 3],[3, 5],[3, 6],[2, 7],[5, 100],[6, 100],[7, 100],[4, 100]],columns=['A','B'])

# 图解
G = nx.from_pandas_edgelist(df,source='A',target='B',create_using=nx.DiGraph())
pos = nx.spring_layout(G)
nx.draw(G,pos,with_labels=True)
plt.show()
pd.Series(list(nx.all_simple_paths(G,1,x)) for x in G.nodes() if G.out_degree(x)==0).explode()

# 递归解
def g(x):
    res = []
    while x:
        res.append(x)
        x = partent[x]
    return res[::-1]

def f(x):
    for i in d[x]:
        if i in d:
            partent[i] = x
            yield from f(i)
        else:
            yield from g(x)
            yield i

def fn(node):
    global d,partent
    d = df.groupby('A').B.agg(list).to_dict()
    partent = {node:None}
    return pd.Series(f(node)).groupby(pd.Series(f(node)).eq(node).cumsum()).agg(list)

fn(1),fn(2)







