class Solution:
    def check(self, haystack, needle, pos, m, n):
        if pos + n > m:
            return False
        for j in range(n):
            if haystack[pos + j] != needle[j]:
                return False
        return True
    
    def hashes(self, s, n, p, M):
        h = [0] * (n + 1)
        pi = 1
        for i in range(n):
            h[i + 1] = (h[i] + pi * (ord(s[i]) - ord('a'))) % M
            pi = (pi * p) % M
        return h
    
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        p = 31
        M = 10 ** 9 + 9
        subhash = lambda h, i, j: (h[j] + M - h[i]) % M
        hhash = self.hashes(haystack, m, p, M)
        nhash = self.hashes(needle, n, p, M)[-1]
        pi = 1
        for i in range(m - n + 1):
            curr = subhash(hhash, i, i + n)
            if curr == (nhash * pi) % M and self.check(haystack, needle, i, m, n):
                return i
            pi = (pi * p) % M
        return -1