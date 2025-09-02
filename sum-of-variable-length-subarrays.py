class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0] * (n + 1)
        for i in range(n):
            res[max(i - nums[i], 0)] += 1
            res[i + 1] -= 1
        for i in range(n):
            res[i + 1] += res[i]
        return sum(res[i] * nums[i] for i in range(n))