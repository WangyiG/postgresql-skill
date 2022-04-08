# 1.给定两个数a和b，要求实现a + abs(b)，但不允许调用abs函数，其中abs是计算绝对值的操作

from operator import add,sub

def a_plus_abs_b(a,b):
    return (sub,add)[b>0](a,b)

a_plus_abs_b(2,-3)   

# 2.给定三个数，要求返回三个数中最大的两个数的平方和，并且只能填写一行代码
def two_of_three(a,b,c):
    return a*a+b*b+c*c-min(a,b,c)*min(a,b,c)

two_of_three(2,3,4)

# 3.给定一个整数n，要求返回除了n本身以外最大的因数,如无则1
def largest_factor(n):
    import math
    for i in range(2,math.ceil(math.sqrt(n))):
        # i最小时,n//i最大
        if n%i == 0:
            return n//i
    return 1

largest_factor(14)

'''
4.实现函数,给定整数n,反复执行如下过程：
如果n是偶数,则除以2
如果n是奇数,则乘3再加上1
如果n等于1,退出

要求:打印出n的变化过程以及返回变化了几次
'''
def hailstone(n):
    step = 1
    while n != 1:
        print(n)
        n = n*3+1 if n%2 else n//2
        step += 1
    print(1)
    return step

hailstone(10)


