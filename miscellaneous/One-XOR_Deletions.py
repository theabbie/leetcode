from collections import Counter


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = float('inf')
    ctr = Counter(arr)
    for el in arr:
        res = min(res, n - ctr[el] - ctr[el ^ 1])
    print(res)