class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        lcp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                lcp[i][j] = 1 + lcp[i + 1][j + 1]
                if s[i] != t[j]:
                    lcp[i][j] = 0
        res = 0
        for i in range(m):
            for j in range(n):
                l = lcp[i][j]
                if i + l < m and j + l < n:
                    res += lcp[i + l + 1][j + l + 1] + 1
        return res