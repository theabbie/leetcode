class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[n - 1] = (1, 1)
        maxlen = 0
        maxctr = 0
        for i in range(n - 1, -1, -1):
            mlen = 0
            mctr = 0
            found = False
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    found = True
                    l, ctr = dp[j]
                    if l > mlen:
                        mlen = l
                        mctr = ctr
                    elif l == mlen:
                        mctr += ctr
            if not found:
                mctr += 1
            dp[i] = (1 + mlen, mctr)
            if 1 + mlen > maxlen:
                maxlen = 1 + mlen
                maxctr = mctr
            elif 1 + mlen == maxlen:
                maxctr += mctr
        return maxctr