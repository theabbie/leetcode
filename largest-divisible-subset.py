class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n
        parent = [None] * n
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] == dp[j] + 1:
                        parent[i] = j
        i = max(range(n), key = lambda x: dp[x])
        res = [i]
        while parent[res[-1]] != None:
            res.append(parent[res[-1]])
        return [nums[i] for i in res]