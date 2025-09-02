class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        s = [0] * (1 << n)
        dp = [[float('inf')] * (k + 1) for _ in range(1 << n)]
        dp[0][0] = 0
        for mask in range(1, 1 << n):
            for i in range(n):
                if mask & (1 << i):
                    s[mask] += cookies[i]
            for rem in range(1, k + 1):
                submask = mask
                while submask:
                    dp[mask][rem] = min(dp[mask][rem], max(s[submask], dp[mask ^ submask][rem - 1]))
                    submask = (submask - 1) & mask
        return dp[-1][k]