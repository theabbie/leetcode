class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        dp = defaultdict(lambda: float('-inf'))
        for i in range(n - 1, -1, -1):
                for j in range(i + 1, n):
                    m = (nums[i] + nums[j]) % k
                    dp[(i, m)] = max(dp[(i, m)], 1 + dp[(j, m)], 2)
                    res = max(res, dp[(i, m)])
        return res