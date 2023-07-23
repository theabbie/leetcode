t = int(input())

def dist(arr, x, y):
    res = 0
    for el in arr:
        res += min((x - el) * (x - el), (y - el) * (y - el))
    return res

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    x = y = 0
    m, M = min(arr), max(arr)
    res = float('inf')
    beg = m
    end = M
    while beg <= end:
        mid = (beg + end) // 2
        a, b = dist(arr, mid, y), dist(arr, mid + 1, y)
        if a <= b:
            res = min(res, a)
            x = mid
            end = mid - 1
        else:
            res = min(res, b)
            x = mid + 1
            beg = mid + 1
    while beg <= end:
        mid = (beg + end) // 2
        a, b = dist(arr, x, mid), dist(arr, x, mid + 1)
        if a <= b:
            res = min(res, a)
            y = mid
            end = mid - 1
        else:
            res = min(res, b)
            y = mid + 1
            beg = mid + 1
    print(res)