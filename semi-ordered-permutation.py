class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        one = nums.index(1)
        last = nums.index(n)
        if one < last:
            return one + n - last - 1
        return one - last + one + n - (one + 1) - 1