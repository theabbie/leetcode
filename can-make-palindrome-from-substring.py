class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        p = [[0] * 26 for _ in range(n + 1)]
        for i in range(n):
            for c in range(26):
                p[i + 1][c] += p[i][c]
            p[i + 1][ord(s[i]) - ord('a')] += 1
        res = []
        for l, r, k in queries:
            odds = 0
            for c in range(26):
                if p[r + 1][c] % 2 != p[l][c] % 2:
                    odds += 1
            res.append(k >= odds // 2)
        return res