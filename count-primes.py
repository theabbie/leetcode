import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0
        numprimes = n - 2
        l = int(math.sqrt(n)) + 1
        for i in range(2, l):
            if primes[i] == 0:
                continue
            for j in range(i, 1 +  n // i):
                if i * j < n and primes[i * j] == 1:
                    primes[i * j] = 0
                    numprimes -= 1
        return numprimes