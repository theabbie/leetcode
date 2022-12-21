from collections import Counter

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if k > m:
        print("NO")
        continue
    pos = True
    ctr = Counter(arr)
    d = m
    prev = 0
    curr = 0
    for el in sorted(ctr.keys()):
        curr += (el - prev) * d
        d -= ctr[el]
        if d > 0 and d < k:
            pos = False
            break
        prev = el
    print("YES" if pos and curr == n else "NO")