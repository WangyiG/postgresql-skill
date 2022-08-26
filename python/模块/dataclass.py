import dataclasses
from dataclasses import dataclass,field

@dataclass
class InventoryItem:
    """dataclass中init默认为True,隐式init了"""
    name: str
    unit_price: float
    quantity_on_hand: int = 1

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

# 与namedtuple相比dataclass支持默认值初始化,支持实例方法操作
x = InventoryItem('apple',16999)
x.total_cost(),dataclasses.asdict(x)


@dataclass
class Player:
    """ 描述球员的类, 记录球员的信息"""
    name: str
    number: int
    position: str
    age: int

@dataclass
class Team:
    """ 描述球队的类，球队包括队名称、队成员"""
    name: str
    players: list[Player]


james = Player('Lebron James', 23, 'SF', 25)  # 实例化一个球员james
davis = Player('Anthony Davis', 3, 'PF', 21)   # 实例化一个球员davis

lal = Team('Los Angeles Lakers', [james, davis])  # 实例化一个球队，将两个球员加入队中

f'Team name:{lal.name},Team merbers:{[_.name for _ in lal.players]}'


# 设置frozen=True,对象初始化后禁止改变,尝试修改value值会报错:cannot assign to field 'value'
@dataclass(frozen=True) 
class Data:
    name: str
    value: int = 42


data = Data('my_name', 99)
# data.value = 1


# 设置order=True,使得实例对象可以参与排序
@dataclass(order=True)
class Data1:
    name:str
    value:int

sorted([Data1('a',2),Data1('a',1)])


# field被用于设置每个成员变量的具体设置:field(*, default=MISSING, default_factory=MISSING, init=True, repr=True,hash=None, compare=True, metadata=None)
# 对于可变类型默认值的设置,使用field的default_factory参数来设置,注意default参数与default_factory不能同时存在
@dataclass
class C:
    # 对于不可变类型默认值,也可以使用field的default参数来设置
    list_name:str = field(default='arr')
    # 引入field,使用默认工厂函数来初始化可变类型默认值
    my_list: list[int] = field(default_factory=list)

c1 = C()
c1.my_list += [1, 2, 3]
c2 = C()

print("c1:{0}; c2:{1}".format(c1, c2))


# field中metadata参数为字段设置附加信息,可以使用fields来获取这些附加信息
@dataclass
class Position:
    name :str
    lon :float = field(default=0.0,metadata={'as_name':'经度','unit':'degrees'})
    lat :float = field(default=0.0,metadata={'as_name':'维度','unit':'degrees'})

p = Position('上海',10.0,20.2)
# 获取lon字段,别名为经度,单位unit为度degrees
fields(p)[1].metadata



# __post_init__方法根据某一属性动态生成其他属性，有点类似@property描述器属性
@dataclass
class Circle:
    r:int

    def __post_init__(self):
        self.area = np.pi*self.r*self.r

c = Circle(1)
c.area

# 示例

import json
from dataclasses import dataclass,field,asdict,fields


@dataclass
class Tree:
    id: int
    name: str
    nodes: list=field(default_factory=list,repr=False) 

    def add(self,id,name):
        self.nodes.append(Tree(id,name))
        # 链式调用add方法china.add(1,'a').add(2,'b').add(3,'c')时,self分别是china,a,b
        return self.nodes[-1]

    @property
    def ids(self):
        # 获取所有id
        ids = [self.id]
        for node in self.nodes:
            ids += node.ids
        return ids

    def get_subtree(self,id):
        # 根据id获取对应子树
        if id in self.ids:
            if self.id == id:
                subtree = asdict(self)
                return subtree
            for node in self.nodes:
                if node.get_subtree(id):
                    return node.get_subtree(id)
        return None

    def get_paths(self,id):
        # 根据id获取id所在主干
        if id in self.ids:
            paths = [self.id]
            for node in self.nodes:
                paths += node.get_paths(id)
            return paths
        return []

    def get_links(self):
        # 获取节点关联数组
        links = []
        for node in self.nodes:
            links.append([node.id,node.name,self.id])
            links += node.get_links()
        return links

 

china = Tree(1,'中国')
china.add(200,'上海').add(201,'黄埔区').add(2011,'人民公园').add(20112,'相亲角')

china.ids,china.get_paths(2011),china.get_links()

china.get_subtree(201)

print(json.dumps(asdict(china),indent=4,ensure_ascii=False))










