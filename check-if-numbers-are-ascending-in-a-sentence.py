class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(t) for t in s.split() if t.isdigit()]
        n = len(nums)
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                return False
        return True