class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [[float('-inf')] * (target + 1) for _ in range(10)]
        dp[0][0] = 0
        for d in range(1, 10):
            for rem in range(target + 1):
                dp[d][rem] = dp[d - 1][rem]
                if cost[d - 1] <= rem:
                    dp[d][rem] = max(dp[d][rem], 1 + max(dp[d - 1][rem - cost[d - 1]], dp[d][rem - cost[d - 1]]))
        res = []
        rem = target
        for d in range(9, 0, -1):
            mx = (-1, -1)
            for ctr in range(rem // cost[d - 1], -1, -1):
                 mx = max(mx, (ctr + dp[d - 1][rem - ctr * cost[d - 1]], ctr))
            if mx[0] != -1:
                res.append(str(d) * mx[1])
                rem -= mx[1] * cost[d - 1]
        return "".join(res) or "0"