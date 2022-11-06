import bisect

n = int(input())

def calculate(p, q):
    mod = 998244353
    expo = mod - 2
    while expo:
        if expo & 1:
            p = (p * q) % mod
        q = (q * q) % mod
        expo >>= 1
    return p

arr = list(map(int, input().split()))

order = []

prev = 0

for k in range(n):
    i = bisect.bisect_left(order, arr[k])
    bisect.insort(order, arr[k])
    prev += arr[k] * (2 * i + 1)
    for j in range(i + 1, k + 1):
        prev += 2 * order[j]
    print(calculate(prev, (k + 1) * (k + 1)))