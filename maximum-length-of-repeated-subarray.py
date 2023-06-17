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
    def isCommon(self, ahash, bhash, m, n, l):
        aset = set()
        for i in range(m - l + 1):
            aset.add((ahash[0].rangeHash(i, i + l - 1), ahash[1].rangeHash(i, i + l - 1)))
        for i in range(n - l + 1):
            if (bhash[0].rangeHash(i, i + l - 1), bhash[1].rangeHash(i, i + l - 1)) in aset:
                return True
        return False
    
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        ahash = [StringHash(nums1, 101, 10 ** 9 + 7), StringHash(nums1, 109, 10 ** 9 + 9)]
        bhash = [StringHash(nums2, 101, 10 ** 9 + 7), StringHash(nums2, 109, 10 ** 9 + 9)]
        beg = 0
        end = min(m, n)
        res = beg
        while beg <= end:
            mid = (beg + end) // 2
            if self.isCommon(ahash, bhash, m, n, mid):
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res