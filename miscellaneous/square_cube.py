t = int(input())

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

def CBRT(N):
    end = 1
    while end * end * end < N:
        end *= 2
    beg = end // 2
    res = 1
    while beg <= end:
        mid = (beg + end) // 2
        if mid * mid * mid <= N:
            res = mid
            beg = mid + 1
        else:
            end = mid - 1
    return res

for i in range(100, 201):
    print(i, SQRT(i) - CBRT(i))

def f(n):
    ctr = {}
    for k in range(n, n + 5):
        curr = SQRT(k) - CBRT(k)
        ctr[curr] = ctr.get(curr, 0) + 1
    return max(ctr.keys(), key = lambda x: ctr[x])

for _ in range(t):
    x = int(input())
    end = 1
    while f(end) < x:
        end *= 2
    beg = end // 2
    res = end
    while beg <= end:
        mid = (beg + end) // 2
        if f(mid) >= x:
            res = mid
            end = mid - 1
        else:
            beg = mid + 1
    print(res)