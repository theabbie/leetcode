from collections import Counter
import bisect

t = int(input())

def bigger(arr, M):
    beg = 0
    end = len(arr) - 1
    res = 0
    while beg <= end:
        mid = (beg + end) // 2
        if arr[mid] <= M:
            beg = mid + 1
        else:
            res = max(res, n - mid)
            end = mid - 1
    return res

def score(keys, values, M, c, d):
    res = 0
    beg = 0
    end = len(keys) - 1
    while beg <= end:
        mid = (beg + end) // 2
        if keys[mid] <= M:
            res = values[mid]
            beg = mid + 1
        else:
            end = mid - 1
    return res

for _ in range(t):
    n, c, d = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ctr = Counter(arr)
    ctr = sorted([[k, v] for k, v in ctr.items()])
    keys = [k for k, v in ctr]
    values = [v for k, v in ctr]
    for i in range(len(ctr)):
        prev = 0
        if i > 0:
            prev = values[i - 1]
        values[i] = prev + c * (values[i] - 1) - d
    res = float('inf')
    for M in arr + list(range(1, n + 1)):
        res = min(res, d * M + score(keys, values, M, c, d) + c * bigger(arr, M))
    print(res)