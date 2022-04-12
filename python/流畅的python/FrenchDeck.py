from collections import namedtuple

'''
namedtuple具名元组:只有属性没有方法的类,
接受2个参数,一参是类名,二参是实例属性名,后者可书写成以空格分隔的字符串也可书写成元组或列表之类的可迭代对象
实例的初始化与普通类一致
'''

Path = namedtuple('path','begin end length')
Path0 = Path('上海','北京','1000公里')

# 可以接受元组列表等可迭代对象,字典只能接受key,且只能按顺序接收
new = ('常州','合肥','300公里')
Path1 = Path._make(new)

Path1._asdict()
# return:{'begin': '常州', 'end': '合肥', 'length': '300公里'}







Card = namedtuple('card',['rank','suit'])

class FrenchDeck:

    # 类属性点数列表与花色列表
    ranks = list(map(str,range(2,11)))+list('JQKA')
    suits = ['spades','diamonds','clubs','hearts']

    # 初始化实例属性_cards,4*13张花色与点数组合的卡牌
    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
            return len(self._cards)
        
    def __getitem__(self,position):
            return self._cards[position]

deck = FrenchDeck()

# deck是FrenchDeck的实例,而deck中的每一张card又都是Card的实例
deck[0],deck[0].rank,deck[0]._asdict()

# return:card(rank='2', suit='spades'), '2', {'rank': '2', 'suit': 'spades'}




