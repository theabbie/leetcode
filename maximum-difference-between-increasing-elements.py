class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mdiff = float('-inf')
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                mdiff = max(mdiff, nums[j] - nums[i])
        return mdiff if mdiff > 0 else -1