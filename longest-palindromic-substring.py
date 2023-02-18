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
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        M = 10 ** 9 + 9
        p = 31
        self.ppow, self.invppow = self.powers(n + 1, p, pow(p, M - 2, M), M)
        subhash = lambda h, i, j: (self.invppow[i] * (h[j + 1] + M - h[i])) % M
        hashes = self.hashes(s, p, M)
        revhashes = self.hashes(s[::-1], p, M)
        for l in range(n, 0, -1):
            for i in range(n - l + 1):
                if subhash(hashes, i, i + l - 1) == subhash(revhashes, n - l - i, n - i - 1):
                    return s[i:i+l]