import sys

sys.setrecursionlimit(10 ** 5)

M = 10 ** 9 + 7

num = input()

def count(num, i, n, sumdiff, ftight, ltight, commontight, cache):
    if i >= n:
        if sumdiff > 0 and not commontight:
            return 1
        return 0
    key = (i, sumdiff, ftight, ltight, commontight)
    if key in cache:
        return cache[key]
    maxfd = maxld = 9
    if ftight:
        maxfd = int(num[i])
    if ltight:
        maxld = int(num[i])
    res = 0
    for digitdiff in range(0 if commontight else -9, 10):
        for fd in range(max(-digitdiff, 0), min(maxld + 1 - digitdiff, maxfd + 1)):
            ld = fd + digitdiff
            res += count(num, i + 1, n, sumdiff + digitdiff, ftight and fd == maxfd, ltight and ld == maxld, commontight and digitdiff == 0, cache)
            res %= M
    cache[key] = res
    return res

print(count(num, 0, len(num), 0, True, True, True, {}))