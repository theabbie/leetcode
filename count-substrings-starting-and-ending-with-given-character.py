class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        k = s.count(c)
        return k * (k + 1) // 2