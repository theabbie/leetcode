class Solution:
    cache = {}
    
    def maxPalindrome(self, s, i, j):
        key = 1100 * i + j
        if (key) in self.cache:
            return self.cache[key]
        if i == j:
            self.cache[key] = 1
        elif s[i] == s[j] and i + 1 == j:
            self.cache[key] = 2
        elif s[i] == s[j]:
            self.cache[key] = self.maxPalindrome(s, i + 1, j - 1) + 2
        else:
            self.cache[key] = max(self.maxPalindrome(s, i, j - 1), self.maxPalindrome(s, i + 1, j))
        return self.cache[key]
        
    def longestPalindromeSubseq(self, s: str) -> int:
        self.cache.clear()
        return self.maxPalindrome(s, 0, len(s) - 1)