class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: (2 if x == 0 else int(x < 0), -abs(x)))
        res = float('-inf')
        p = 1
        for el in nums:
            p *= el
            res = max(res, p)
        return res