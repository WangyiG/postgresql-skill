'''
电商领域有个功能明显可以使用“策略”模式，即根据客户的属性或订单中的商品计算折扣。
假如一个网店制定了下述折扣规则:
有 1000 或以上积分的顾客，每个订单享 5% 折扣。
同一订单中，单个商品的数量达到 20 个或以上，享 10% 折扣。
订单中的不同商品达到 10 个或以上，享 7% 折扣。
简单起见，我们假定一个订单一次只能享用一个折扣。
'''
from collections import namedtuple
# 每一个顾客具有姓名和积分属性
Customer = namedtuple('Customer', 'name fidelity')

# 每一种商品具有品名,数量,单价等属性,总金额通过total方法实现
class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    def total(self):
        return self.price * self.quantity
      
      
# 定义一个订单类,订单实例传入顾客,购物车产品列表,折扣方法(没错,属性可以是一个方法),可执行总金额方法与折扣后金额方法,其中总金额方法实际是生成总金额属性,折扣后金额方法调用了总金额方法,输出打印总金额与折扣后金额
class Order: 
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount
    def __repr__(self):
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'
      
      
# 定义折扣方法,Order的实例order的due方法调用promotion方法,promotion方法又调用实例的customer属性,cart属性与total方法,其中customer属性与cart属性又分别去调用Customer具名元组与LineItem类
def fidelity_promo(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0
def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount
def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0
  
  
# 测试
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
banana_cart = [LineItem('banana', 30, .5),LineItem('apple', 10, 1.5)]
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
Order(joe, banana_cart, fidelity_promo),Order(ann, long_order, fidelity_promo)


# 选择最优策略,折扣方法返回的都是折扣额然后在due中被总金额减,即折扣越大则越优
promos  = [fidelity_promo, bulk_item_promo, large_order_promo]
def best_promo(order):
    return max(promo(order) for promo in promos)

Order(joe, banana_cart, best_promo),Order(ann, long_order, best_promo)



