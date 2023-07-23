import sys

sys.setrecursionlimit(10 ** 5)

t = int(input())

M = 10 ** 9 + 7

def count(arr, i, n, curr, k, cache):
    currcount = "{:b}".format(curr).count("1")
    if i >= n:
        return 1 if currcount == k else 0
    key = (i, curr)
    if key in cache:
        return cache[key]
    res = count(arr, i + 1, n, curr, k, cache)
    res += count(arr, i + 1, n, curr & arr[i], k, cache)
    res %= M
    cache[key] = res
    return res

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count(arr, 0, n, arr[0], k, {}))