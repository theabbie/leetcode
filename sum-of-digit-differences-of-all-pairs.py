from collections import *

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for _ in range(11):
            ctr = Counter()
            total = 0
            for i in range(n):
                res += total - ctr[nums[i] % 10]
                ctr[nums[i] % 10] += 1
                total += 1
                nums[i] //= 10
        return res