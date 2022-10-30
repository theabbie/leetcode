t = int(input())

def isPal(s, i, j, cache):
    if i >= j:
        return True
    if (i, j) in cache:
        return cache[(i, j)]
    res = s[i] == s[j - 1] and isPal(s, i + 1, j - 1, cache)
    cache[(i, j)] = res
    return res

for tt in range(1, t + 1):
    n = int(input())
    s = input()
    j = 1
    cache = {}
    while j < n and (not isPal(s, 0, j, cache) or not isPal(s, j, n, cache)):
        j += 1
    print(f"Case #{tt}: {s[:j]}")