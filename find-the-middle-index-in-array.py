class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        total = sum(nums)
        curr = 0
        if curr * 2 == total - nums[0]:
            return 0
        for i in range(n - 1):
            curr += nums[i]
            if curr * 2 == total - nums[i + 1]:
                return i + 1
        return -1