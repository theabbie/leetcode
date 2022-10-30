import sys

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

arr = list(map(int, input().split()))

def minSub(arr, i, n, rem, last, cache):
    if rem < 0:
        return float('inf')
    if i >= n:
        if rem == 0:
            return 0
        return float('inf')
    key = (i, rem, last)
    if key in cache:
        return cache[key]
    k = 1
    if last:
        k = 0
    a = minSub(arr, i + 1, n, rem - arr[i], False, cache)
    b = k + minSub(arr, i + 1, n, rem, True, cache)
    res = min(a, b)
    cache[key] = res
    return res

cache = {}

for i in range(1, m + 1):
    curr = minSub(arr, 0, n, i, False, cache)
    if curr == float('inf'):
        print(-1)
    else:
        print(curr)