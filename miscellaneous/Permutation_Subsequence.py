from collections import Counter

M = 10 ** 9 + 7

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ctr = Counter(arr)
    curr = Counter()
    res = 0
    currval = 1
    for i in range(1, n + 1):
        curr[i] += ctr[i]
        currval *= ctr[i]
        currval %= M
        res += currval
        res %= M
    print(res)