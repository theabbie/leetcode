class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        res = 0
        x = 0
        for el in nums:
            x += el
            if x == 0:
                res += 1
        return res