class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        M = max(nums)
        ctr = [0] * (M + 1)
        for el in nums:
            ctr[el] += 1
        mctr = [0] * (M + 1)
        for i in range(1, M + 1):
            mul = 1
            while i * mul <= M:
                mctr[i] += ctr[i * mul]
                mul += 1
        dp = [0] * (M + 1)
        for i in range(M, 0, -1):
            dp[i] = mctr[i] * (mctr[i] - 1) // 2
            mul = 2
            while i * mul <= M:
                dp[i] -= dp[i * mul]
                mul += 1
        q = len(queries)
        queries = [(queries[i], i) for i in range(q)]
        queries.sort()
        res = [0] * q
        i = 0
        less = 0
        for pos, qpos in queries:
            while i <= M and less + dp[i] <= pos:
                less += dp[i]
                i += 1
            res[qpos] = i
        return res