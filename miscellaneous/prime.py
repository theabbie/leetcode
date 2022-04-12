import math

class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def factorial(self, n):
        if n == 1:
            return 1
        return n * self.factorial(n - 1)

    def numPrimeArrangements(self, n: int) -> int:
        numPrimes = 0
        for i in range(1, n + 1):
            if self.isPrime(i):
                numPrimes += 1
        return (self.factorial(numPrimes) * self.factorial(n - numPrimes)) % (10 ** 9 + 7)