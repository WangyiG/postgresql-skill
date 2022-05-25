# data
arr = [['张不黑', '张九同', '白衣'],
       ['张改革', '张不黑', '白衣'],
       ['张国防', '张九同', '白衣'],
       ['张大王', '张小举', '榜眼'],
       ['张夏', '张国庆', '镖师'],
       ['张九哥', '张不黑', '进士'],
       ['张小举', '张九同', '举人'],
       ['张春', '张国庆', '武夫'],
       ['张开放', '张源', '武举人'],
       ['张秋', '张国庆', '武师'],
       ['张源', '张老黑', '武士'],
       ['张国庆', '张老黑', '武状元'],
       ['张绣', '张小举', '秀才'],
       ['张九同', '张老祖', '状元']]
df = pd.DataFrame(arr,columns=['人名','父母','身份'])

# 从最后一辈推父辈,为什么从后往前,因为子辈只有一个父辈,而父辈可能有多个子辈
child = df['人名'][~df['人名'].isin(df['父母'].tolist())]

# 映射
parent = df.set_index('人名')['父母'].to_dict()
info = df.set_index('人名')['身份'].to_dict()

# 递归的将子辈与父辈及父辈的父辈从右向左添加到列表中
def father_son(x):
    return [parent[x],x] if parent[x] not in parent else [*father_son(parent[x]),x]

# result
child.map(father_son).agg(pd.Series).assign(work=child.map(info))
