from collections import Counter

n = int(input())

arr = list(map(int, input().split()))

MAX = 1 + max(arr)

v = [False] * MAX
sp = [0] * MAX

for i in range(2, MAX, 2):
    sp[i] = 2

for i in range(3, MAX, 2):
    if not v[i]:
        sp[i] = i
        j = i
        while j * i < MAX:
            if not v[j * i]:
                v[j * i] = True
                sp[j * i] = i
            j += 2

res = n * (n - 1) // 2

ctr = [0] * MAX

for el, f in Counter(arr).items():
    curr = el
    prev = -1
    primes = []
    while curr > 1:
        if sp[curr] != prev:
            primes.append(sp[curr])
            prev = sp[curr]
        curr //= sp[curr]
    m = len(primes)
    for mask in range(1, 1 << m):
        p = 1
        sign = -1
        for i in range(m):
            if mask & (1 << i):
                p *= primes[i]
                sign *= -1
        res -= sign * ctr[p] * f
        ctr[p] += f
    if el != 1:
        res -= f * (f - 1) // 2

print(res)