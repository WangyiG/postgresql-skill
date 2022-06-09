from jsonpath import jsonpath

data = {
    "store": {
        "book": [{"category": "参考", "author": "Nigel Rees", "title": "世纪风俗","price": 8.95},
                 {"category": "小说","author": "Evelyn Waugh","title": "荣誉剑","price": 12.99},
                 {"category": "小说","author": "Herman Melville","title": "Moby Dick","isbn": "0-553-21311-3","price": 8.99},
                 {"category": "小说","author": "JRR Tolkien","title": "指环王","isbn": "0-395-19395-8", "price": 22.99}],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}


'''
$ : 根元素
@ : 当前元素
.或[,] : 子元素,其中[,]允许使用name和slice切片索引,jsonpath的索引也是从0开始
.. : 递归下降
* : 通配符
?() : 过滤表达式
() : 脚本表达式
'''
# 最后一本书的名字,不支持负值索引使用脚本表达式(@.length-1)
jsonpath(data,'$.store.book[(@.length-1)]')

# 不支持单个负值索引但支持反向切片式索引
jsonpath(data,'$.store.book[-2:]')

# 支持枚举索引
jsonpath(data, '$..book[0,3]') 

# 当book的层级比较深时,可无需关注父元素分别是啥,使用递归下降$..book[(@.length-1)]
jsonpath(data,'$..book[(@.length-1)]')

# 所有书的作者
jsonpath(data,'$..author') == jsonpath(data,'$..*.author')

# ?(过滤表达式),注意不要漏掉@.
jsonpath(data,'$..[?(@.title=="指环王")]')

jsonpath(data,'$..book[?(@.price>15)]')





