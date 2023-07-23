t = int(input())

def score(x):
    mind = float('inf')
    maxd = float('-inf')
    while x:
        d = x % 10
        maxd = max(maxd, d)
        mind = min(mind, d)
        x //= 10
    return maxd - mind

for _ in range(t):
    a, b = map(int, input().split())
    res = (score(a), a)
    for x in range(a, a + 101):
        if x <= b:
            res = max(res, (score(x), x))
    for x in range(b - 100, b + 1):
        if x >= a:
            res = max(res, (score(x), x))
    print(res[1])