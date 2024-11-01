class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs[0])
        @lru_cache(maxsize = None)
        def dp(i, prev):
            if i >= m:
                return 0
            take = True
            for s in strs:
                if prev != -1 and s[prev] > s[i]:
                    take = False
                    break
            res = dp(i + 1, prev)
            if take:
                res = max(res, 1 + dp(i + 1, i))
            return res
        return m - dp(0, -1)