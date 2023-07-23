import sys

sys.setrecursionlimit(10 ** 7)

n = int(input())

M = 998244353

div5 = pow(5, M - 2, M)

cache = {}

def prob(i):
    if i == n:
        return 1
    if i > n:
        return 0
    if i in cache:
        return cache[i]
    res = prob(i * 2) + prob(i * 3) + prob(i * 4) + prob(i * 5) + prob(i * 6)
    res *= div5
    res %= M
    cache[i] = res
    return res

print(prob(1))