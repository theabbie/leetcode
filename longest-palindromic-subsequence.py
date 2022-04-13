class Solution:
    cache = {}
    
    def maxPalindrome(self, s, i, j):
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        if i == j:
            self.cache[(i, j)] = 1
        elif s[i] == s[j] and i + 1 == j:
            self.cache[(i, j)] = 2
        elif s[i] == s[j]:
            self.cache[(i, j)] = self.maxPalindrome(s, i + 1, j - 1) + 2
        else:
            self.cache[(i, j)] = max(self.maxPalindrome(s, i, j - 1), self.maxPalindrome(s, i + 1, j))
        return self.cache[(i, j)]
        
    def longestPalindromeSubseq(self, s: str) -> int:
        self.cache = {}
        return self.maxPalindrome(s, 0, len(s) - 1)