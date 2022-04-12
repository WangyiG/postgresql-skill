# 题目描述:找一个三角形数组自下而上的和的最小路径2->4->1->3,每一步只能移动到下一行中相邻的点上,即第三行5可以且只可以移动至2或4,6可以且只可以移动至4或3
x = [
    [2],
    [3,4],
    [5,6,1],
    [2,4,3,5]
]


class Node:
    # 给实例添加累和属性sum与路径属性path
    def __init__(self,sum,path):
        self.sum = sum
        self.path = path

    # 根据左右下级节点更新sum属性与path属性,选择较小值更新sum及拼接对应路径到path,注意字符串拼接的顺序
    def addSub(self,x,y):
        if x.sum>y.sum:
            self.sum += y.sum
            self.path = '->右'+y.path
        else:
            self.sum += x.sum
            self.path = '->左'+x.path
            
 

# 1.自下而上,最下级节点层初始化实例
nodesSub = [Node(k,'') for k in x[-1]]

for i in range(1,len(x)):
    # 2.上级节点层初始化实例
    nodes = [Node(k,'') for k in x[-i-1]]
    for k in range(len(nodes)):
        # 3.对于上级节点层的每个节点,其下级左右节点的下标分别是其下标与下标+1,根据下级左右节点执行实例方法,逐个更新上级节点层的每个节点
        nodes[k].addSub(nodesSub[k],nodesSub[k+1])
    # 4.自下而上,自下而上,上级节点层根据下级节点层更新完毕,角色转换为下级节点层被更上级节点层调用
    nodesSub = nodes

print('最短路径',nodes[0].sum)
print('路径方向：开始',nodes[0].path)

# 最短路径 10
# 路径方向：开始 ->右->右->左





