from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    d = arr[-1] - arr[0]
    res = 0
    ctr = Counter()
    for el in arr:
        res += 2 * ctr[el - d]
        if d != 0:
            res += 2 * ctr[el + d]
        ctr[el] += 1
    print(res)