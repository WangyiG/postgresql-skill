d,f = pd.read_excel(r"C:\Users\wangy\Desktop\根据排名及意愿安排入学.xlsx",None).values()
d,f

parent = f.set_index('学校名称').招生数.to_dict()

def fn(x):
    for i in x:
        if parent[i]:
            parent[i] -= 1
            return i
    else:
        return '名落孙山'
      
d.set_index(['积分排名','姓名']).droplevel(0).agg(fn,axis=1).reset_index()
