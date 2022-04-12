class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        k = len(nums)
        curr = [1]
        n = 1
        for i in range(k - 1):
            curr = [0] + curr
            n += 1
            for i in range(n - 1):
                curr[i] = curr[i] + curr[i + 1]
        total = 0
        for i in range(k):
            total += nums[i] * curr[i]
        return total % 10