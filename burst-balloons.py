class Solution:
    def score(self, nums, i, j, n):
        if i > j:
            return 0
        if i == j:
            l = 1 if i == 0 else nums[i - 1]
            r = 1 if i == n - 1 else nums[i + 1]
            return l * nums[i] * r
        if self.cache[i][j] != -1:
            return self.cache[i][j]
        res = 0
        for k in range(i, j + 1):
            l = 1 if i == 0 else nums[i - 1]
            r = 1 if j == n - 1 else nums[j + 1]
            res = max(res, l * nums[k] * r + self.score(nums, i, k - 1, n) + self.score(nums, k + 1, j, n))
        self.cache[i][j] = res
        return res
    
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        self.cache = [[-1] * n for _ in range(n)]
        return self.score(nums, 0, n - 1, n)