df = pd.DataFrame([['A', 'B', np.nan],
                   ['C', 'D', np.nan],
                   ['E', 'G', np.nan],
                   ['B', 'C', 'R'],
                   ['A', 'B', 'D'],
                   ['F', 'G', np.nan],
                   ['G', 'H', np.nan],
                   ['X', 'Y', np.nan],
                   ['Y', 'X', np.nan],
                   ['Y', 'Z', np.nan],
                   ['Z', 'J', np.nan],
                   ['S', 'T', np.nan],
                   ['R', 'Q', np.nan],
                   ['W', 'T', np.nan]])

def f(x):
    for i in m:
        if x&i and i-x:
            x = f(x|i)
    return x
m = df.agg(lambda x:set(x.dropna()),axis=1).tolist()
df.assign(new=df.agg(lambda x:f(set(x.dropna())),axis=1)).fillna('')
