import math

t = int(input())

def prime_sieve(n):
    flag = n % 6 == 2
    sieve = bytearray((n // 3 + flag >> 3) + 1)
    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
    return sieve


def prime_list(n):
    res = []
    if n > 1:
        res.append(2)
    if n > 2:
        res.append(3)
    if n > 4:
        sieve = prime_sieve(n + 1)
        res.extend(3 * i + 1 | 1 for i in range(1, (n + 1) // 3 + (n % 6 == 1)) if not (sieve[i >> 3] >> (i & 7)) & 1)
    return res

nums = []

for _ in range(t):
    n = int(input())
    nums.append(n)

N = max(nums)
primes = prime_list(1 + max(min(N, 4 * (10 ** 6)), 1000))

def getres(n):
    for p in primes:
        if n % p == 0:
            if n % (p * p) == 0:
                return [p, n // (p * p)]
            else:
                return [int(math.sqrt(n // p)), p]

for n in nums:
    print(*getres(n))