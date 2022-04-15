from math import hypot

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x},{self.y})'
    def __str__(self):
        return f'{self.x},{self.y}'
    def __abs__(self):
        return hypot(self.x,self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self,other):
        x = self.x+other.x
        y = self.y+other.y
        return Vector(x,y)
    def __mul__(self,scalar):
        return Vector(self.x*scalar,self.y*scalar)
      
'''
两个输出方法都是为了改变对象实例的输出,让其更有可读性,避免出现类似<Vector object at 0x10e100070>这种不明其意的输出
__str__方法会被print与str函数使用
__repr__方法会被终端或解释器使用,且当对象未未实现__str__方法时会被print使用
综上所述,自己编写类时不考虑str函数的使用,写一个__repr__既能被解释器调用也能被print调用,更精简方便
'''
print(Vector(3,4))
str(Vector(3,4)),Vector(3,4)  


'''
对只使用了自身实例属性的特殊方法,可以以不带下划线的方式把实例对象当做参数直接调用,如__bool__直接使用了abs(self)而非__abs__(self),如上文中可以直接使用str,如下文一会会直接使用bool
这里__bool__特殊方法,也可以直接定义返回为return bool(self.x or self.y),即只有实例的模或者说实例的2个属性均为0,才返回False
上面说到bool(object)的实现,实际是调用的object的__bool__方法,而对于哪些未实现__bool__方法的object来说,则会去尝试调用object.__len__方法,若为0则返回False
为什么len是特殊方法?背后的原因是CPython会直接从一个C 结构体里读取对象的长度属性,完全不会调用任何方法。换句话说,len之所以不是一个普通方法,是为了让 Python自带的数据结构可以走后门，
abs也是同理,也多亏了它是特殊方法,使得我们可以把 len用于自定义数据类型。
'''
class Test:
    def __init__(self,x):
        self.x = x
    def __len__(self):
        if isinstance(self.x,int):
            return len(str(self.x))
        return len(self.x)

bool(Test(0)),bool(Test(''))


'''
__add__为Vector类实现了2个实例的+操作
__mul__为Vector类实现了向量与标量相乘,改变模的大小或标量为负时,不仅改变大小还改变向量方向
值得注意的是,这两个方法的返回值都是新创建的向量对象,被操作的两个向量(self 或 other)还是原封不动,代码里只是读取了它们的值而已,中缀运算符的基本原则就是不改变操作对象,而是产出一个新的值
另外上面的Vector类只实现了向量与标量的乘,未能实现乘法的交换律,即标量*向量会报错,将在13章中使用__rmul__来解决这个问题
'''
Vector(3,4)*2





