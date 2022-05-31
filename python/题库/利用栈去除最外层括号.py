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



