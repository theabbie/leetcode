class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        l = 2 * k + 1
        total = 0
        for i in range(n):
            total += nums[i]
            if i >= l:
                total -= nums[i - l]
            if i >= l - 1:
                res[i - k] = total // l
        return res