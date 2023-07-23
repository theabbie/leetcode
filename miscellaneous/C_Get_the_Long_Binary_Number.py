import math
import sys

sys.setrecursionlimit(10 ** 5)

t = int(input())

def find(num, i, n, k, tight, ones, zeroes, res, cache):
    if i >= n:
        return zeroes - ones == k
    key = (i, tight, ones)
    if key in cache:
        return cache[key]
    mind = 0
    if tight:
        mind = int(num[i])
    for d in range(mind, 2):
        res[i] = str(d)
        if find(num, i + 1, n, k, tight and d == mind, ones + int(d == 1), zeroes + int(d == 0), res, cache):
            cache[key] = True
            return True
        res[i] = ""
    cache[key] = False
    return False

for _ in range(t):
    n, k = map(int, input().split())
    arr = input()
    res = [""] * n
    found = find(arr, 0, n, k, True, 0, 0, res, {})
    if not found:
        x = k + 2 * math.ceil(max(n - k, 0) / 2)
        if x <= n:
            x += 2
        res = ["1"] + ["0"] * (x - 1)
        for i in range((x - k) // 2 - 1):
            res[-(i + 1)] = "1"
    print("".join(res))