def f(x):
    a,res = [],''
    for i in x:
        if i==')':
            a.pop()
            if a:
                res+=')'
        else:
            if a:
                res+='('
            a.append(i)
    return res


pd.DataFrame(['(())','(()()(()))','(()())(())','(()())(())(()(()))()'],columns=['a']).assign(b=lambda x:x.a.map(f))



def g(x):
    a,res = [],''
    for i in x:
        if i==')':
            a.pop()
        #  非空栈判断的顺序卡在i判断之间,导致不方便简单的if else   
        if a:
            res+=i
        if i=='(':
            a.append(i)


    return res
            

g('(((())))(()())')




