import sys

sys.setrecursionlimit(10 ** 6)

a, x, m = map(int, input().split())

def getpow(a, x, m, cache):
    if x == 0:
        return 1 % m
    if x in cache:
        return cache[x]
    k = (x + 1) // 2
    res = (getpow(a, k - 1, m, cache) + pow(a, k, m) * getpow(a, x - k, m, cache)) % m
    cache[x] = res
    return res

print(getpow(a, x - 1, m, {}))