import sys

sys.setrecursionlimit(10 ** 5)

cache = {}

def getsum(n):
    if n == 1:
        return 1
    if n in cache:
        return cache[n]
    parent = n // 2
    res = n + getsum(parent)
    cache[n] = res
    return res

t = int(input())

for _ in range(t):
    n = int(input())
    print(getsum(n))