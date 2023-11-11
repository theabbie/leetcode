class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        p = 0
        res = 0
        for el in nums:
            p += el
            if p > 0:
                res += 1
        return res