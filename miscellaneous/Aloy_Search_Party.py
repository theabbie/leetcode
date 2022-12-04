import collections
i=input
t=int(i())
while t:
    n,t=int(i()),t-1
    v=collections.Counter([i() for _ in range(n)])
    print(sum(v[x]*(v[x]-1)//2 for x in v))