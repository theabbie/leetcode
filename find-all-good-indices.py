class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dec = [1] * n
        inc = [1] * n
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                dec[i] = dec[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                inc[i] = inc[i + 1] + 1
        res = []
        for i in range(k, n - k):
            if dec[i - 1] >= k and inc[i + 1] >= k:
                res.append(i)
        return res