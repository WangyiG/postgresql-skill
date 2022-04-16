# heapq堆数据结构最重要的特征是heap[0]永远是最小的元素,堆分最小堆与最大堆,heapq库中的堆默认是最小堆
import heapq
# 入堆
heap = []
heapq.heappush(heap,2)
heapq.heappush(heap,4)
heapq.heappush(heap,1)
# 出堆,弹出最小值,注意这里虽然打印出来顺序是142,但实际出堆遵循从小到大出堆
print(heap)
heapq.heappop(heap),heapq.heappop(heap),heapq.heappop(heap)


# 列表转化为堆,这是一个原地操作 
nums = [3,7,5,6]
heapq.heapify(nums)
[heapq.heappop(nums) for _ in range(len(nums))]

# heapq.merge顺序迭代合并后的排序迭代对象,生成的是一个迭代器,要求参数都是升序列表
for i in heapq.merge([2,4,8],[3,5,6,7],[1,7]):
    print(i) 
    
 
# heapq.heapreplace(heap.item),删除并返回(弹出)最小元素值,添加新的元素值
nums = [2,4,6,8]
heapq.heapreplace(nums,3),nums


# heapq.heappushpop(heap,item),比较item与heap[0]的大小,如果item小则弹出item,如果item大则执行heapq.heapreplace操作
nums = [2,4,6,8]
heapq.heappushpop(nums,1),nums,heapq.heappushpop(nums,3),nums


# heapq.nlargest(n,heap[,key]),heapq.nsmallest(n,heap[,key])获取堆中极大与极小的n个元素
info = [{'name':'a','age':17},{'name':'c','age':14},{'name':'e','age':13},{'name':'d','age':15},{'name':'b','age':18}]
heapq.nlargest(3,info,key=lambda x:x['name']),heapq.nsmallest(3,info,key=lambda x:x['age'])


# 对于带权重的元组记录实现权重排序,应将权重做为元组的第一条记录
info = [(4,'a'),(2,'c'),(3,'b')]
heapq.heapify(info)
heapq.heappop(info)


# 利用heapq实现一个优先级队列
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item):
        heapq.heappush(self._queue, item)
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)

    def heapify(self,item):
        heapq.heapify(item)
        self._queue = item

q = PriorityQueue()
items = [(4,'a'),(2,'b'),(5,'c'),(3,'d')]
for item in items:
    q.push(item)
q.pop(),q.pop()

t = PriorityQueue()
info = [(4,'a'),(2,'b'),(5,'c'),(3,'d')]
t.heapify(info)
t.pop(),t.pop()



