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
import dataclasses
from dataclasses import dataclass,field,asdict

@dataclass
class Tree:
    id: int
    name: str
    children: dict=field(default_factory=dict)
    
    def add(self,id,name):
        if isinstance(name,str):
            self.children[id] = Tree(id,name)
        elif isinstance(name,Tree):
            self.children[id].children[id] = Tree(id,name)

        return self.children[id]

    @property
    def ids(self):
        def f(x):
            for k,v in x.items():
                if isinstance(v,dict):
                    yield from f(v)
                if k == 'id':
                    yield v
        return list(f(asdict(self)))
    
    
    
china = Tree(1,'中国')
sichuan = china.add(id=510000, name='四川省')
_ = sichuan.add(id=510700, name='绵阳市')
_ = sichuan.children[510700].add(id=510703, name='涪城区')
_ = sichuan.children[510700].add(id=510704, name='游仙区')


print(json.dumps(asdict(china),indent=4,ensure_ascii=False))

china.ids,sichuan.ids










