import sys

sys.setrecursionlimit(10 ** 6)

def count(num, i, n, tight, nz, k, cache):
    if i >= n:
        if nz == k:
            return 1
        return 0
    key = (i, tight, nz)
    if key in cache:
        return cache[key]
    md = 9
    if tight:
        md = int(num[i])
    res = 0
    for d in range(md + 1):
        res += count(num, i + 1, n, tight and d == md, nz + (1 if d != 0 else 0), k, cache)
    cache[key] = res
    return res

n = input()
k = int(input())

print(count(n, 0, len(n), True, 0, k, {}))