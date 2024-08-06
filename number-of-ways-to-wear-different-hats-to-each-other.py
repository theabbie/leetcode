class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        M = 10 ** 9 + 7
        n = len(hats)
        TARGET = (1 << n) - 1
        vals = {}
        for i in range(n):
            for h in hats[i]:
                if h not in vals:
                    vals[h] = []
                vals[h].append(i)
        vals = list(vals.values())
        @lru_cache(maxsize = None)
        def count(i, mask):
            if i >= len(vals):
                return int(mask == TARGET)
            res = count(i + 1, mask)
            for j in vals[i]:
                if not mask & (1 << j):
                    res += count(i + 1, mask | (1 << j))
                    res %= M
            return res
        return count(0, 0)