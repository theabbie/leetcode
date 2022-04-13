class Solution:
    def isPalindrome(self, s, i, j):
        if (i, j) in self.PalCache:
            return self.PalCache[(i, j)]
        val = False
        if i >= j - 1:
            val = s[i] == s[j - 1]
        elif s[i] == s[j - 1]:
            val = self.isPalindrome(s, i + 1, j - 1)
        self.PalCache[(i, j)] = val
        return val
    
    def mcuts(self, s, i, n):
        if i == n:
            return -1
        if i in self.cache:
            return self.cache[i]
        mincuts = n - i - 1
        for j in range(i + 1, n + 1):
            if self.isPalindrome(s, i, j):
                val = self.mcuts(s, j, n)
                mincuts = min(mincuts, 1 + val)
        self.cache[i] = mincuts
        return mincuts
    
    def minCut(self, s: str) -> int:
        self.cache = {}
        self.PalCache = {}
        n = len(s)
        return self.mcuts(s, 0, n)