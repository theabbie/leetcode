class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        M = 10 ** 9 + 7
        n = len(s)
        primes = "2357"
        isPrime = False
        isComp = False
        for c in s:
            if c in primes:
                isPrime = True
            else:
                isComp = True
        if not isPrime or not isComp:
            return 0
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[n][0] = 1
        primesum = [[0] for _ in range(k + 1)]
        primesum[0][0] = 1
        for i in range(n - 1, -1, -1):
            if s[i] in primes:
                for l in range(1, k + 1):
                    if minLength <= len(primesum[l - 1]):
                        dp[i][l] += primesum[l - 1][-minLength]
            for l in range(k + 1):
                val = 0
                if s[i] in primes and (i == 0 or s[i - 1] not in primes):
                    val = dp[i][l]
                primesum[l].append(primesum[l][-1] + val)
        return dp[0][k] % M