class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        res = (float('inf'), "")
        for i in range(n):
            ctr = 0
            for j in range(i, n):
                ctr += int(s[j])
                if ctr == k:
                    res = min(res, (j - i + 1, s[i : j + 1]))
        return res[1]