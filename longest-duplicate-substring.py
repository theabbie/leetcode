class Solution:
    def powers(self, n, p, ip, M):
        pw = 1
        invpw = 1
        ppow = []
        invppow = []
        for _ in range(n):
            ppow.append(pw)
            invppow.append(invpw)
            pw = (pw * p) % M
            invpw = (invpw * ip) % M
        return ppow, invppow
    
    def hashes(self, s, p, M):
        n = len(s)
        h = [0] * (n + 1)
        for i in range(n):
            h[i + 1] = (h[i] + self.ppow[i] * (ord(s[i]) - ord('a'))) % M
        return h
    
    def check(self, s, a, b, n):
        for i in range(n):
            if s[a + i] != s[b + i]:
                return False
        return True
    
    def possible(self, s, hashes, subhash, n, k):
        seen = {}
        for i in range(n - k + 1):
            curr = subhash(hashes, i, i + k - 1)
            if curr in seen and self.check(s, seen[curr], i, k):
                return s[seen[curr] : seen[curr] + k]
            seen[curr] = i
        return None
    
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        M = 10 ** 9 + 9
        p = 31
        self.ppow, self.invppow = self.powers(n + 1, p, pow(p, M - 2, M), M)
        subhash = lambda h, i, j: (self.invppow[i] * (h[j + 1] + M - h[i])) % M
        hashes = self.hashes(s, p, M)
        beg = 1
        res = ""
        end = n
        while beg <= end:
            mid = (beg + end) // 2
            curr = self.possible(s, hashes, subhash, n, mid)
            if curr != None:
                res = curr
                beg = mid + 1
            else:
                end = mid - 1
        return res