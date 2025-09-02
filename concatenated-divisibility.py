class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pow10 = [pow(10, len(str(x)), k) for x in nums]
        dp = [dict() for _ in range(1 << n)]
        dp[0][0] = []
        for mask in range(1 << n):
            for rem, seq in list(dp[mask].items()):
                for i in range(n):
                    if not mask & (1 << i):
                        nm = mask | (1 << i)
                        nr = (rem * pow10[i] + nums[i]) % k
                        cand = seq + [nums[i]]
                        if nr not in dp[nm] or cand < dp[nm][nr]:
                            dp[nm][nr] = cand
        full = (1 << n) - 1
        return dp[full].get(0, [])