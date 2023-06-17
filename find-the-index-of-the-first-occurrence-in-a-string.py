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
        self.p = p
        self.mod = mod
        self.ppow, self.invppow = Number.primepowers(len(s) + 1, self.p, self.mod)
        self.hashvals = self.hashes(s)
        
    def hashes(self, s):
        n = len(s)
        h = [0] * (n + 1)
        for i in range(n):
            h[i + 1] = (h[i] + self.ppow[i] * (ord(s[i]) - ord('a'))) % self.mod
        return h
    
    def rangeHash(self, i, j):
        return (self.invppow[i] * (self.hashvals[j + 1] + self.mod - self.hashvals[i])) % self.mod

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        hayhash = [StringHash(haystack, 31, 10 ** 9 + 7), StringHash(haystack, 37, 10 ** 9 + 9)]
        needlehash = (StringHash(needle, 31, 10 ** 9 + 7).rangeHash(0, n - 1), StringHash(needle, 37, 10 ** 9 + 9).rangeHash(0, n - 1))
        for i in range(m - n + 1):
            if (hayhash[0].rangeHash(i, i + n - 1), hayhash[1].rangeHash(i, i + n - 1)) == needlehash:
                return i
        return -1