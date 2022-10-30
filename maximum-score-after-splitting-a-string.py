class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        total = s.count("1")
        curr = 0
        res = 0
        for i in range(n - 1):
            if s[i] == "1":
                total -= 1
            else:
                curr += 1
            res = max(res, curr + total)
        return res