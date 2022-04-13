class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        T = [[False for i in range(n + 1)] for j in range(m + 1)]
        T[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                T[0][j] = T[0][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    T[i][j] = T[i - 1][j - 1]
                elif p[j - 1] == "*":
                    T[i][j] = T[i][j - 1] or T[i - 1][j]
        return T[m][n]