class Solution:
    def countKConstraintSubstrings(self, s: str, k: int):
        n = len(s)
        j = n - 1
        pf = [[0, 0] for _ in range(n + 1)]
        for i in range(n):
            pf[i + 1][0] = pf[i][0] + int(s[i] == '0')
            pf[i + 1][1] = pf[i][1] + int(s[i] == '1')
        res = 0
        for i in range(n - 1, -1, -1):
            while j > i and min(pf[j + 1][1] - pf[i][1], pf[j + 1][0] - pf[i][0]) > k:
                j -= 1
            res += j - i + 1
        return res