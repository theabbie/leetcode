class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        N = max(max(r) for r in nums)
        primes = [True] * (N + 1)
        primes[0] = primes[1] = False
        i = 0
        while i * i <= N:
            if primes[i]:
                j = i * i
                while j <= N:
                    primes[j] = False
                    j += i
            i += 1
        res = 0
        m = len(nums)
        n = len(nums[0])
        for i in range(m):
            for j in range(n):
                if i - j == 0 or i + j == n - 1:
                    if primes[nums[i][j]]:
                        res = max(res, nums[i][j])
        return res