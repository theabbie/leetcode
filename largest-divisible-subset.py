from collections import *

def gcd(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
    return x

def memodict(f):
    """memoization decorator for a function taking a single argument"""
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__

def pollard_rho(n):
    """returns a random factor of n"""
    if n & 1 == 0:
        return 2
    if n % 3 == 0:
        return 3

    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            prev = p
            p = (p * p) % n
            if p == 1:
                return gcd(prev - 1, n)
            if p == n - 1:
                break
        else:
            for i in range(2, n):
                x, y = i, (i * i + 1) % n
                f = gcd(abs(x - y), n)
                while f == 1:
                    x, y = (x * x + 1) % n, (y * y + 1) % n
                    y = (y * y + 1) % n
                    f = gcd(abs(x - y), n)
                if f != n:
                    return f
    return n

@memodict
def prime_factors(n):
    """returns a Counter of the prime factorization of n"""
    if n <= 1:
        return Counter()
    f = pollard_rho(n)
    return Counter([n]) if f == n else prime_factors(f) + prime_factors(n // f)

def distinct_factors(n):
    """returns a list of all distinct factors of n"""
    factors = [1]
    for p, exp in prime_factors(n).items():
        factors += [p**i * factor for factor in factors for i in range(1, exp + 1)]
    return factors

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = defaultdict(int)
        prev = {}
        mx = (1, nums[0])
        for el in nums:
            for f in distinct_factors(el):
                if f == el:
                    if el == 1:
                        dp[el] = 1
                    continue
                dp[el] = max(dp[el], 1 + dp[f])
                if dp[el] > 1 and dp[el] == 1 + dp[f]:
                    prev[el] = f
                mx = max(mx, (dp[el], el))
        res = [mx[1]]
        while res[-1] in prev:
            res.append(prev[res[-1]])
        res.reverse()
        return res