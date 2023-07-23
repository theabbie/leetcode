from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = n * (n - 1) // 2
    ctr = Counter(arr)
    for el in ctr:
        res -= ctr[el] * (ctr[el] - 1) // 2
    print(res)