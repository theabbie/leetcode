class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        res = 0
        val = lambda x: abs(ord(s[x]) - ord(t[x]))
        i = 0
        cost = 0
        for j in range(n):
            cost += val(j)
            while i < j and cost > maxCost:
                cost -= val(i)
                i += 1
            if cost <= maxCost:
                res = max(res, j - i + 1)
        return res