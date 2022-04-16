# bisect模块实现了二分查找和插入算法,四个参数有:seq为一个升序序列,x为需要在seq中定位的值,lo指定查找区间的start默认为0,指定查找区间的stop默认为len(seq)
import bisect

x = 200
list1 = [1, 3, 6, 24, 55, 78, 454, 555, 1234, 6900]
bisect.bisect(list1, x)

x = 200
list1 = [1, 3, 6, 24, 55, 78, 454, 555, 1234, 6900]
# 这是一步原地执行操作,返回值为None
bisect.insort(list1, x)
list1

import random
random.seed(1)
print('New  Pos Contents')
print('---  --- --------')
l = []
for i in range(1, 15):
    v = random.randint(1, 100)
    position = bisect.bisect(l, v)
    bisect.insort(l, v)
    print(f'{v:>3}{position:>4}  ', l)
    

# 实现类似pd.cut功能
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]
[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
