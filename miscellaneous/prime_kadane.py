n = 100

primes = [True] * (n + 1)

primes[0], primes[1] = False, False

for i in range(n + 1):
    if primes[i]:
        j = 2
        while i * j <= n:
            primes[i * j] = False
            j += 1

plist = []

for i in range(n + 1):
    if primes[i]:
        plist.append(i)

k = len(plist)
for i in range(k):
    if i % 2 == 1:
        plist[i] *= -1

maxTillNow = 0
maxSoFar = float('-inf')

for el in plist:
    maxTillNow = max(el + maxTillNow, el)
    maxSoFar = max(maxSoFar, maxTillNow)

print(maxSoFar)