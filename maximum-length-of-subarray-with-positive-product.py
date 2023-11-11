class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        prev = [n, n]
        res = 0
        p = 0
        prev[0] = -1
        for i in range(n):
            if nums[i] == 0:
                prev[0] = i
                prev[1] = n
                p = 0
                continue
            p += int(nums[i] < 0)
            p %= 2
            res = max(res, i - prev[p])
            prev[p] = min(prev[p], i)
        return res