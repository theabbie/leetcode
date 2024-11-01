M = 10 ** 9 + 7

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        MX = max(nums)
        dp = [1] * (MX + 1)
        ndp = [0] * (MX + 1)
        pf = [0] * (MX + 2)
        def update():
            pf[0] = 0
            for i in range(MX + 1):
                pf[i + 1] = pf[i] + dp[i]
        update()
        for i in range(n - 1, -1, -1):
            up = 0 if i == 0 else nums[i - 1]
            for prev in range(up + 1):
                prevdec = float('inf')
                if i > 0:
                    prevdec = nums[i - 1] - prev
                low = max(prev, nums[i] - prevdec)
                ndp[prev] = 0
                if nums[i] + 1 >= low:
                    ndp[prev] = pf[nums[i] + 1] - pf[low]
                    ndp[prev] %= M
            dp, ndp = ndp, dp
            update()
        return dp[0]