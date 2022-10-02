from collections import Counter

t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    ctr = Counter(arr)
    res = 0
    for o in ctr:
        if ctr[o] >= c:
            res += c
        else:
            res += ctr[o]
    print(res)