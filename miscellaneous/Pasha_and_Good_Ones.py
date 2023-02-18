from collections import defaultdict

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    res = 0
    for curr in set(s):
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] += p[i] + (1 if curr == s[i] else 0)
        extra = 0
        if k < 0:
            for i in range(n + k + 1):
                if p[i - k] - p[i] == 0:
                    extra += 1
        pos = defaultdict(int)
        for j in range(n + 1):
            p[j] = 2 * p[j] - j
            res += pos[p[j] - k]
            pos[p[j]] += 1
        res -= extra
    print(res)