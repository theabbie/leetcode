class Solution:
    def longest(self, p, last, i, j, k):
        if j - i < k:
            return 0
        for x in range(26):
            if 0 < p[j][x] - p[i][x] < k:
                mid = last[i][x]
                a = self.longest(p, last, i, mid, k)
                b = self.longest(p, last, mid + 1, j, k)
                return max(a, b)
        return j - i
    
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        p = [[0] * 26 for _ in range(n + 1)]
        last = [[n] * 26 for _ in range(n + 1)]
        self.pos = lambda c: ord(c) - ord('a')
        for i in range(n):
            for x in range(26):
                p[i + 1][x] += p[i][x]
                if x == self.pos(s[i]):
                    p[i + 1][x] += 1
        for i in range(n - 1, -1, -1):
            for x in range(26):
                last[i][x] = last[i + 1][x]
                if x == self.pos(s[i]):
                    last[i][x] = i
        return self.longest(p, last, 0, n, k)