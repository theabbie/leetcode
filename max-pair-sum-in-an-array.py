class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        for i in range(n):
            for j in range(i + 1, n):
                x = max(str(nums[i]))
                y = max(str(nums[j]))
                if x == y:
                    res = max(res, nums[i] + nums[j])
        return res