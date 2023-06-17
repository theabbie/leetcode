class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        res = 0
        p = 0
        for el in nums:
            p += el
            if p > 0:
                res += 1
        return res