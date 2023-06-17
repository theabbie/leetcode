class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = 0
        for i in range(n):
            p = max(p, nums[i])
            nums[i] += p
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums