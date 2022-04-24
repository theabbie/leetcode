from functools import lru_cache

t = int(input())

@lru_cache(maxsize=None)
def numPalindromic(n):
    if n == 1:
        return 1
    for i in range(2, n + 1):
        if n % i == 0:
            return 1 + numPalindromic(n // i)

for tt in range(1, t + 1):
    n = int(input())
    print(f"Case #{tt}: {numPalindromic(n)}")
