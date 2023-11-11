import sys

sys.setrecursionlimit(10 ** 5)

M = 998244353

s = input()

cache = [[-1] * (len(s) + 1) for _ in range(len(s))]

mp = {"(": 1, ")": -1}

def count(s, i, n, p):
    if i >= n:
        return int(p == 0)
    if cache[i][p] != -1:
        return cache[i][p]
    res = 0
    if s[i] == "?":
        res += count(s, i + 1, n, p + 1)
        if p > 0:
            res += count(s, i + 1, n, p - 1)
    elif p + mp[s[i]] >= 0:
        res += count(s, i + 1, n, p + mp[s[i]])
    res %= M
    cache[i][p] = res
    return res

print(count(s, 0, len(s), 0))