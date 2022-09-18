class Solution:
    def getprefix(self, s, n):
        z = [0] * n
        d = 0
        for i in range(1, n):
            while d and s[d] != s[i]:
                d = z[d - 1]
            d += s[i] == s[d]
            z[i] = d
        return z
    
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        z = self.getprefix(s + "#" + s[::-1], 2 * n + 1)
        if z[-1] == n:
            return s
        return s[z[-1]-n:][::-1] + s