import math

n, m = map(int, input().split())

def SQRT(N):
    end = 1
    while end * end < N:
        end *= 2
    beg = end // 2
    res = 1
    while beg <= end:
        mid = (beg + end) // 2
        if mid * mid <= N:
            res = mid
            beg = mid + 1
        else:
            end = mid - 1
    return res

def getprod(n, m):
    if n * n < m:
        return -1
    if m <= n:
        return m
    res = float('inf')
    k = SQRT(m) + 1
    for i in range(m // n, k + 1):
        j = math.ceil(m / i)
        if 1 <= j <= n:
            res = min(res, i * j)
    return res

print(getprod(n, m))