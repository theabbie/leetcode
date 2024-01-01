class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        pos = {}
        res = 0
        p = 0
        pos[p] = 0
        for i in range(n):
            if s[i] in "aeiou":
                p ^= 1 << "aeiou".index(s[i])
            if p not in pos:
                pos[p] = i + 1
            else:
                res = max(res, i + 1 - pos[p])
        return res