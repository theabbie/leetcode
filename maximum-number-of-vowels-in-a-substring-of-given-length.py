class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        v = 0
        res = 0
        for i in range(n):
            if s[i] in "aeiou":
                v += 1
            if i >= k and s[i - k] in "aeiou":
                v -= 1
            res = max(res, v)
        return res