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


from collections.abc import Iterable,Iterator
# 可迭代iterable与迭代器iterator,迭代器一定是可迭代的,但可迭代的比如列表,并不是迭代器,yield或通过生成器表达式构建的生成器一定是迭代器,但迭代器并不一定都是生成器,iterable>iterator>generator
print(isinstance([0],Iterable),isinstance([0],Iterator))
print(isinstance(iter([0]),Iterable),isinstance(iter([0]),Iterator))

# 接着回到FrenchDeck类中来，如上FrenchDeck类中并没有实现__iter__方法,那么实例deck是可迭代的吗？
print(isinstance(deck,Iterable))
# 返回了False,那貌似是不可迭代的,再试试for循环遍历
for i in deck:
    print(i)
    break
# for循环可以遍历,那么这又是怎么一回事呢,原来只有通过迭代器协议__iter__方法实现的迭代才能被collections.abc.Iterable检测
# __getitem__方法实现的迭代虽不能被检测,但可被遍历,并且__getitem__实现的迭代是可索引的,而迭代器协议实现的迭代不必是可索引的,比如字典与集合,所以{0,1}[0]会报错
# __iter__是遍历可迭代对象的首选方法。如果未定义，解释器将尝试使用__getitem__来模拟其行为
# 以deck实例来说,它的可索引是由属性_cards这个列表代理实现,可以很方便的通过索引取出rank为A的Card
deck[12::13]








