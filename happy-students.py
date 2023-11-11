class Solution:
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        i = 0
        for choose in range(n + 1):
            while i < n and nums[i] < choose:
                i += 1
            if i == choose and (i == n or nums[i] > choose):
                res += 1
        return res