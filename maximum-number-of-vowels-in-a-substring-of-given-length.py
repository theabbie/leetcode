class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        v = 0
        for i in range(k):
            if s[i] in "aeiou":
                v += 1
        res = v
        for i in range(n - k):
            if s[i] in "aeiou":
                v -= 1
            if s[i + k] in "aeiou":
                v += 1
            res = max(res, v)
        return res