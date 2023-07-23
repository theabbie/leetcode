from collections import Counter

t = int(input())

res = []

for _ in range(t):
    n = int(input())
    arr = sorted(map(int, input().split()))
    ctr = [0] * (n + 1)
    for el, f in Counter(arr).items():
        mul = 1
        while el * mul <= n:
            ctr[el * mul] += f
            mul += 1
    res.append(max(ctr))

print(*res)