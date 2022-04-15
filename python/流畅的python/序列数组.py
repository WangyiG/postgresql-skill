'''
按序列元素的数据类型是否要求一致,可将序列分为:
容器序列:list,tuple,collections.deque等,序列中存放的是所包含的任意数据类型的引用
扁平序列:str,bytes,memoryview,array.array,序列中存放的是值而非引用,在内存中使用一段连续的内存空间,优点是紧凑高效,缺点是只能操作单一基础数据类型

序列类型还能按照能否被修改来分类:
可变序列:list,array.array,collections.deque,memoryview等,变量对应的值可以被原地修改(可变类型通常都有对应的原地修改操作如lise的append,set的add),并且原地修改后内存地址仍保持不变
不可变序列:str,bytes,tuple,变量对应的值不可被原地修改,只能重新赋值从而分配新的内存空间。
可变序列更灵活,不可变类型更安全,对于可变数据类型主要影响的操作有copy(仍是引用)与deepcopy(开辟新内存空间),函数参数传递时,内部原地修改对外部的影响
'''
