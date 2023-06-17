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
            h[i + 1] = (h[i] + self.ppow[i] * s[i]) % self.mod
        return h
    
    def rangeHash(self, i, j):
        return (self.invppow[i] * (self.hashvals[j + 1] + self.mod - self.hashvals[i])) % self.mod

class Solution:
    def possible(self, prefs, k):
        subs = None
        for pref in prefs:
            n = len(pref)
            curr = set()
            for i in range(len(pref[0].hashvals) - k):
                curr.add((pref[0].rangeHash(i, i + k - 1), pref[1].rangeHash(i, i + k - 1)))
            if subs == None:
                subs = curr
            else:
                subs &= curr
        return subs == None or len(subs) > 0
    
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        prefs = []
        end = float('inf')
        for path in paths:
            prefs.append([StringHash(path, 10 ** 9 + 7, 10 ** 9 + 9), StringHash(path, 10 ** 9 + 9, 10 ** 9 + 7)])
            end = min(end, len(path))
        beg = 1
        res = 0
        while beg <= end:
            mid = (beg + end) // 2
            if self.possible(prefs, mid):
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res