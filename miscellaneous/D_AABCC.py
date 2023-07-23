import bisect

N = 1 + 10 ** 6

sp = [1] * N
v = [False] * N

for i in range(2, N, 2):
    sp[i] = 2

for i in range(3, N, 2):
    if not v[i]:
        sp[i] = i
        j = i
        while j * i < N:
            v[j * i] = True
            sp[j * i] = i
            j += 2

plist = []

for i in range(2, N):
    if sp[i] == i:
        plist.append(i)

m = len(plist)

n = int(input())

res = 0

i = 2

while i * i <= n:
    primes = []
    curr = i
    while curr > 1:
        primes.append(sp[curr])
        curr //= sp[curr]
    if len(primes) == 2:
        low = primes[0] + 1
        high = min(primes[1] - 1, n // (primes[0] * primes[0] * primes[1] * primes[1]))
        if low <= high:
            res += bisect.bisect_right(plist, high) - bisect.bisect_left(plist, low)
    i += 1
    
print(res)