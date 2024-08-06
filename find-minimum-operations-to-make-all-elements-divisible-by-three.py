class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for el in nums:
            res += min((el % 3), 3 - (el % 3))
        return res