class Solution:
    def encode(self, s: str) -> str:
        n = len(s)
        @lru_cache(maxsize = None)
        def dp(s):
            if s == "":
                return ""
            res = s
            for l in range(1, len(s)):
                j = 0
                ctr = 0
                while j + l <= n and s[j:j+l] == s[:l]:
                    j += l
                    ctr += 1
                    curr = (f"{ctr}[{dp(s[:l])}]" if ctr > 1 else dp(s[:l])) + dp(s[j:])
                    if len(curr) < len(res):
                        res = curr
            return res
        res = dp(s)
        if len(res) >= len(s):
            res = s
        return res