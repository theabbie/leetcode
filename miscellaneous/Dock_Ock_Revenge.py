i=input
r=range
t=int(i())
ai=lambda:list(map(int,i().split()))
for _ in r(t):
    n=int(i())
    a,b=ai(),ai()
    start = 0
    end = n - 1
    for j in range(n):
        if (a[j] != b[j]):
            start = j
            break
    for j in range(n - 1, -1, -1):
        if (a[j] != b[j]):
            end = j
            break
    a[start:end + 1] = reversed(a[start:end + 1])
    print(a)