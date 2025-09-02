class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        dp = [[[float('inf')] * (op2 + 1) for _ in range(op1 + 1)] for _ in range(n + 1)]
        for x in range(op1 + 1):
            for y in range(op2 + 1):
                dp[n][x][y] = 0
        for i in range(n - 1, -1, -1):
            for x in range(op1 + 1):
                for y in range(op2 + 1):
                    dp[i][x][y] = nums[i] + dp[i + 1][x][y]
                    if x > 0:
                        dp[i][x][y] = min(dp[i][x][y], (nums[i] + 1) // 2 + dp[i + 1][x - 1][y])
                    if y > 0 and nums[i] >= k:
                        dp[i][x][y] = min(dp[i][x][y], (nums[i] - k) + dp[i + 1][x][y - 1])
                    if x > 0 and y > 0:
                        v = float('inf')
                        if (nums[i] + 1) // 2 >= k:
                            v = min(v, (nums[i] + 1) // 2 - k)
                        elif nums[i] >= k:
                            v = min(v, (nums[i] - k + 1) // 2)
                        dp[i][x][y] = min(dp[i][x][y], v + dp[i + 1][x - 1][y - 1])
        return dp[0][op1][op2]