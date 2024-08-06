class Solution:
    def longest(self, p, last, i, j):
        for x in range(26):
            if (p[j][x] - p[i][x] > 0) != (p[j][x + 26] - p[i][x + 26] > 0):
                mid = min(last[i][x], last[i][x + 26])
                a = self.longest(p, last, i, mid)
                b = self.longest(p, last, mid + 1, j)
                if a[0] >= b[0]:
                    return a
                return b
        return (j - i, i, j)
    
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        p = [[0] * 52 for _ in range(n + 1)]
        last = [[n] * 52 for _ in range(n + 1)]
        self.pos = lambda c: ord(c) - ord('a') if c.islower() else 26 + ord(c) - ord('A')
        for i in range(n):
            for x in range(52):
                p[i + 1][x] += p[i][x]
                if x == self.pos(s[i]):
                    p[i + 1][x] += 1
        for i in range(n - 1, -1, -1):
            for x in range(52):
                last[i][x] = last[i + 1][x]
                if x == self.pos(s[i]):
                    last[i][x] = i
        res = self.longest(p, last, 0, n)
        return s[res[1]:res[2]]