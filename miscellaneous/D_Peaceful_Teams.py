from collections import defaultdict

def count(i, n, hates, teams, t, cache):
    if i >= n:
        for j in range(t):
            if teams[j] == 0:
                return 0
        return 1
    key = tuple([i] + sorted(teams))
    if key in cache:
        return cache[key]
    res = 0
    for j in range(t):
        valid = True
        for k in hates[i]:
            if teams[j] & (1 << k):
                valid = False
                break
        if valid:
            teams[j] |= 1 << i
            res += count(i + 1, n, hates, teams, t, cache)
            teams[j] &= ~(1 << i)
    cache[key] = res
    return res

n, t, m = map(int, input().split())

hates = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())
    hates[a - 1].add(b - 1)
    hates[b - 1].add(a - 1)

f = 1

for i in range(1, t + 1):
    f *= i

print(count(0, n, hates, [0 for _ in range(t)], t, {}) // f)