import sys

nums = list(map(int, sys.stdin.read().split("\n")))

N = max(nums) + 1

primes = [True] * N
primes[0] = primes[1] = False

for i in range(N):
    if primes[i]:
        j = 2
        while i * j < N:
            primes[i * j] = False
            j += 1

def factors(n):
    yield "1"
    for i in range(2, n + 1):
        if primes[i]:
            while n % i == 0:
                yield str(i)
                n = n // i

for n in nums:
    print(' x '.join(factors(n)))