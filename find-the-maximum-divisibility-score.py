class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res = (float('inf'), -1)
        for d in divisors:
            ctr = 0
            for el in nums:
                if el % d == 0:
                    ctr += 1
            res = min(res, (-ctr, d))
        return res[1]