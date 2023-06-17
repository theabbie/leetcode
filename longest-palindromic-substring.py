class Number:
    def primepowers(N, p, mod):
        ip = pow(p, mod - 2, mod)
        pw = 1
        invpw = 1
        ppow = []
        invppow = []
        for _ in range(N):
            ppow.append(pw)
            invppow.append(invpw)
            pw = (pw * p) % mod
            invpw = (invpw * ip) % mod
        return ppow, invppow

class StringHash:
    def __init__(self, s, p, mod):
        self.n = len(s)
        self.p = p
        self.mod = mod
        self.ppow, self.invppow = Number.primepowers(len(s) + 1, self.p, self.mod)
        self.hashvals, self.revhashvals = self.hashes(s)
        
    def hashes(self, s):
        n = len(s)
        h = [0] * (n + 1)
        rh = [0] * (n + 1)
        for i in range(n):
            h[i + 1] = (h[i] + self.ppow[i] * (ord(s[i]) - ord('a'))) % self.mod
            rh[i + 1] = (rh[i] + self.ppow[i] * (ord(s[n - i - 1]) - ord('a'))) % self.mod
        return h, rh
    
    def rangeHash(self, i, j):
        return (self.invppow[i] * (self.hashvals[j + 1] + self.mod - self.hashvals[i])) % self.mod
    
    def revRangeHash(self, i, j):
        i, j = self.n - j - 1, self.n - i - 1
        return (self.invppow[i] * (self.revhashvals[j + 1] + self.mod - self.revhashvals[i])) % self.mod

class Solution:
    def checkpal(self, hash, n, l):
        for i in range(n - l + 1):
            if hash.rangeHash(i, i + l - 1) == hash.revRangeHash(i, i + l - 1):
                return (i, i + l)
        return False
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        hash = StringHash(s, 31, 10 ** 9 + 7)
        res = (0, (0, 0))
        beg = 0
        end = (n - 1) // 2
        while beg <= end:
            mid = (beg + end) // 2
            curr = self.checkpal(hash, n, 2 * mid + 1)
            if curr:
                res = max(res, (2 * mid + 1, curr))
                beg = mid + 1
            else:
                end = mid - 1
        beg = 1
        end = n // 2
        while beg <= end:
            mid = (beg + end) // 2
            curr = self.checkpal(hash, n, 2 * mid)
            if curr:
                res = max(res, (2 * mid, curr))
                beg = mid + 1
            else:
                end = mid - 1
        return s[res[1][0]:res[1][1]]