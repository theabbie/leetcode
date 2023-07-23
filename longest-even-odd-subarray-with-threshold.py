class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            prev = 1
            mx = float('-inf')
            for j in range(i, n):
                mx = max(mx, nums[j])
                if mx <= threshold and nums[j] % 2 != prev:
                    res = max(res, j - i + 1)
                    prev = nums[j] % 2
                else:
                    break
        return res