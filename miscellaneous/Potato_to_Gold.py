from collections import Counter

t = int(input())

M = 10 ** 9 + 7

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(Counter([el % k for el in arr]))
    res = 1
    ctr = Counter()
    subcount = Counter()
    for i in range(n):
        d = arr[i] % k
        x = ctr[(k - d) % k]
        curr = 0
        curr += (1 << i) - 0
        subcount[d] += curr
        res += curr
        ctr[d] += 1
    print(res % M)