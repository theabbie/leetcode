from collections import defaultdict

t = int(input())

def getDist(arr, i, j, cache):
    if i == j:
        return 0
    if (i, j) in cache:
        return cache[(i, j)]
    res = 1 + getDist(arr, arr[i] - 1, j, cache)
    cache[(i, j)] = res
    return res

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = []
    cache = {}
    for i in range(n):
        res.append(1 + getDist(arr, arr[i] - 1, i, cache))
    print(*res)