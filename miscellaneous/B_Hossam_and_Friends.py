from collections import defaultdict

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    next = defaultdict(lambda: n)
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if b < a:
            next[b] = min(next[b], a)
        if a < b:
            next[a] = min(next[a], b)
    res = 0
    for i in range(n):
        end = next[i]
        j = i
        while j < end and next[j] >= end:
            j += 1
        res += j - i
        i += 1
    print(res)