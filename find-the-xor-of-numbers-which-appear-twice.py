class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = 0
        for el in set(nums):
            if nums.count(el) == 2:
                res ^= el
        return res