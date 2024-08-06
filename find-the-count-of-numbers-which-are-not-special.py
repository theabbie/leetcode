import bisect

MAX = 100001

primes = [True] * MAX
primes[0] = primes[1] = False
i = 0
while i * i <= MAX:
    if primes[i]:
        mul = 2
        while i * mul < MAX:
            primes[i * mul] = False
            mul += 1
    i += 1
            
vals = [i * i for i in range(2, MAX) if primes[i]]

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        return r - l + 1 - bisect.bisect_right(vals, r) + bisect.bisect_left(vals, l)