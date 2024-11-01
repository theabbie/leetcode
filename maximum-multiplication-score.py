class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        @lru_cache(maxsize = None)
        def dp(i, j):
            if j >= 4:
                return 0
            if i >= len(b):
                return float('-inf')
            return max(a[j] * b[i] + dp(i + 1, j + 1), dp(i + 1, j))
        return dp(0, 0)