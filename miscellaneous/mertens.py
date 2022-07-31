mertens = {}

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

def gen(plist, curr, i, n, ctr, lim, mertens):
    if ctr > lim:
        return
    mertens[curr] = 1 - 2 * ctr % 2
    for j in range(i + 1, n):
        gen(plist, curr * plist[i], j, n, ctr + 1, lim, mertens)

gen(plist, 1, 0, len(plist), 0, 3, mertens)