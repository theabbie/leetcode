class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()
        @lru_cache(maxsize = None)
        def dp(i, rem):
            if rem < 0:
                return float('inf')
            if i >= n:
                return 0
            res = float('inf')
            median = i
            sv = 2 * houses[i]
            lv = 2
            s = 0
            for j in range(i, n):
                lv -= 1
                sv -= houses[j]
                while median < (i + j) // 2:
                    median += 1
                    sv += 2 * houses[median]
                    lv += 2
                cost = houses[median] * lv - sv
                res = min(res, cost + dp(j + 1, rem - 1))
            return res
        return dp(0, k)