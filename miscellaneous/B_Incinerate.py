import math

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))
    vals = [(h[i], p[i]) for i in range(n)]
    vals.sort()
    minval = [float('inf')] * n
    minval[-1] = vals[-1][1]
    for i in range(n - 2, -1, -1):
        minval[i] = min(minval[i + 1], vals[i][1])
    print(vals)
    subbed = 0
    for i in range(n):
        if vals[i][0] - subbed > k:
            subbed += k
            k -= minval[i]
    if subbed < minval[-1]:
        
    else:
        print("YES")
