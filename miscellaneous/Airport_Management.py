from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ctr = defaultdict(int)
    for el in a:
        ctr[el] += 1
        ctr[el + 1] -= 1
    for el in b:
        ctr[el] += 1
        ctr[el + 1] -= 1
    res = 0
    curr = 0
    for x, y in sorted(ctr.items()):
        curr += y
        res = max(res, curr)
    print(res)