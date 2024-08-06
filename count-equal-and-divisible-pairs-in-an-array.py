from collections import *

class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ctr = defaultdict(Counter)
        for i in range(1, k + 1):
            mul = 0
            while i * mul < n:
                ctr[i][nums[i * mul]] += 1
                mul += 1
        res = 0
        for i in range(n):
            val = k // self.gcd(k, i)
            res += ctr[val][nums[i]]
            if (i * i) % k == 0:
                res -= 1
        return res // 2