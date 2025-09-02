class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        dp = [0] * k
        for a in nums:
            ndp = [0] * k
            am = a % k
            ndp[am] += 1
            for r in range(k):
                if dp[r]:
                    ndp[(r * am) % k] += dp[r]
            for r in range(k):
                res[r] += ndp[r]
            dp = ndp
        return res