'''
async定义协程函数,协程函数在调用时不会执行,而会生成协程对象,当把协程对象添加到事件循环中函数才会被执行
await关键字后面接的必须是可等待对象,如协程对象,task对象,Future对象,另外需要注意的是await关键字一定是包含在async函数之中的
事件循环:创建一个微任务队列,判断微任务状态,阻塞则进入队列,可执行则弹出队列,直到任务全部弹出队列,队列为空则跳出循环
'''

import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return 'func_end'

async def func1():
    print(3)
    await asyncio.sleep(2)
    print(4)
    return 'func1_end'

async def main():
    print('main_start')

    # create_task需要队列创建之后才能添加任务,name参数可以对任务命名,py推荐这种添加任务的方式
    task_list = [asyncio.create_task( func(),name='f' ),asyncio.create_task( func1(),name='g' )]

    print('main_end')

    # timeout参数可以指定等待时间,等待时间前执行完的会存入done集合,未执行完的会存入pending集合
    done,pending = await asyncio.wait(task_list,timeout=None)

    print(*done,sep='\n')

# asyncio.run( main() )
# jupyter中,直接await主函数即可
await main()


'''
concurrent.futures.Future基于线程池进程池的Future对象
协程概念较新,有些仅支持基于concurrent的异步
'''
import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor

res = []
def f(value):
    time.sleep(1)
    res.append(value*2)
    # 如果end='\n'输出结果会很乱,因为打印end也成了一个微任务
    print(f'{value}->',end='')

# 创建线程池
pool = ThreadPoolExecutor(max_workers=5)

# 创建进程池
# pool = ProcessPoolExecutor(max_workers=5)

for i in range(10):
    fut = pool.submit(f,i)

# 如果正常执行,10个数每个数的出来都需要1秒,需要10秒+,这里并行执行显然并不需要10秒+,应该怎样知道所有数据已经处理完了呢？
time.sleep(3)
res


# gather可以自动将协程对象转换为task,省去create_task,返回一个列表
import asyncio

async def func():
    print(1)
    await asyncio.sleep(3)
    print(2)
    return 'func_end'

async def func1():
    print(3)
    await asyncio.sleep(3)
    print(4)
    return 'func1_end'

async def main():
    print('main_start')
    # timeout参数可以指定等待时间,等待时间前执行完的会存入done集合,未执行完的会存入pending集合
    done = await asyncio.gather(func(),func1())
    print('main_end')

    print(done)

# 创建事件循环并将main任务添加进去,asyncio.run( main() )
# jupyter中,直接await主函数即可
await main()


import threading
from time import ctime,sleep

import asyncio

async def Music(name):

        print ("Begin listening to {name}. {time}".format(name=name,time=ctime()))
        await asyncio.sleep(3)
        print("end listening {time}".format(time=ctime()))

async def Blog(title):

        print ("Begin recording the {title}. {time}".format(title=title,time=ctime()))
        await asyncio.sleep(5)
        print('end recording {time}'.format(time=ctime()))

async def main1(a,b):
        done = await asyncio.gather(Music(a),Blog(b))
        print("all over %s" %ctime())

await main1('FILL ME','')


from joblib import Parallel,delayed

def f(x):
    sleep(2)
    return x*2

sum(Parallel(n_jobs=6)(delayed(f)(i) for i in range(6)))


