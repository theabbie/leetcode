M = 998244353

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    lctr = set()
    rctr = set()
    mx = float('-inf')
    for i in range(n):
        mx = max(mx, arr[i])
        if mx == arr[i]:
            lctr.add(i)
    mn = float('inf')
    for i in range(n - 1, -1, -1):
        mn = min(mn, arr[i])
        if mn == arr[i]:
            rctr.add(i)
    x = len(set.intersection(lctr, rctr))
    if x < n:
        print(pow(2, x, M))
    else:
        print((pow(2, x, M) + M - 1) % M)