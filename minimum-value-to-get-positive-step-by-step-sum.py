class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        p = 0
        res = 1
        for el in nums:
            p += el
            if p <= 0:
                res = max(res, -p + 1)
        return res