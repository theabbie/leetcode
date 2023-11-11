import bisect

MAX = 5 * 10 ** 6
primes = [True] * MAX
primes[0] = primes[1] = False
i = 0
while i * i <= MAX:
    if primes[i]:
        mul = i
        while i * mul < MAX:
            primes[i * mul] = False
            mul += 1
    i += 1
plist = [i for i in range(MAX) if primes[i]]

class Solution:
    def countPrimes(self, n: int) -> int:
        return bisect.bisect_left(plist, n)