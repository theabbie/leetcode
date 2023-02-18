class Solution:
    def hashes(self, s, n, p, M):
        h = [0] * (n + 1)
        pi = 1
        for i in range(n):
            h[i + 1] = (h[i] + pi * (ord(s[i]) - ord('a'))) % M
            pi = (pi * p) % M
        return h
    
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        p = 31
        M = 10 ** 9 + 9
        pw = [1]
        for _ in range(n - 1):
            pw.append((pw[-1] * p) % M)
        fhashes = self.hashes(s, n, p, M)
        rhashes = self.hashes(s[::-1], n, p, M)
        subhash = lambda h, i, j: (h[j + 1] + M - h[i]) % M
        l = 0
        for i in range(n):
            fhash = subhash(fhashes, 0, i)
            rhash = subhash(rhashes, n - i - 1, n - 1)
            fhash = (fhash * pw[n - i - 1]) % M
            if fhash == rhash:
                l = i + 1
        return s[l:][::-1] + s