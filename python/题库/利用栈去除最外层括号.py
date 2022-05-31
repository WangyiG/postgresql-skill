def f(x):
    a,res = [],''
    def g():
        nonlocal a,res
        for i in x:
            if i==')':
                a.pop()
                if a:
                    res += i
            else:
                if a:
                    res += i
                a.append(i)
        return res
    return g()

pd.DataFrame(['(())','(()()(()))','(()())(())','(()())(())(()(()))()'],columns=['a']).assign(b=lambda x:x.a.map(f))
