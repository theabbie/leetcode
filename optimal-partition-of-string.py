class Solution:
    def partitionString(self, s: str) -> int:
        n = len(s)
        seen = set()
        res = 1
        for i in range(n):
            if s[i] in seen:
                res += 1
                seen.clear()
            seen.add(s[i])
        return res