from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    vals = [(arr[i] // (i + 1), arr[i] % (i + 1), i + 1) for i in range(n)]
    ctr = defaultdict(list)
    for x, rem, k in vals:
        if x > 0:
            ctr[x].append((rem, k))
    print(dict(ctr))