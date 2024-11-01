class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        def cost(i, j):
            if i > j:
                return 1
            return 0
        @lru_cache(maxsize = None)
        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            res = 1 + min(dp(i, j - 1), dp(i + 1, j))
            for k in range(i, j):
                if arr[k] == arr[j]:
                    res = min(res, cost(k + 1, j - 1) + dp(i, k - 1) + dp(k + 1, j - 1))
            for k in range(i + 1, j + 1):
                if arr[i] == arr[k]:
                    res = min(res, cost(i + 1, k - 1) + dp(i + 1, k - 1) + dp(k + 1, j))
            return res
        return dp(0, n - 1)