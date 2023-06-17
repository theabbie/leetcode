from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        nums = Counter([(value + (el % value)) % value for el in nums])
        for i in range(max(value, n) + 1):
            if nums[i % value] > 0:
                nums[i % value] -= 1
            else:
                return i