class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        x = 1
        for el in nums:
            if el == x:
                x += 1
        return x