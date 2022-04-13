class Solution:
    def maxPalindrome(self, s, i, j):
        if i == j:
            return 1
        if s[i] == s[j] and i + 1 == j:
            return 2
        if s[i] == s[j]:
            return self.maxPalindrome(s, i + 1, j - 1) + 2
        else:
            return max(self.maxPalindrome(s, i, j - 1), self.maxPalindrome(s, i + 1, j))
    
    def maxProduct(self, s: str) -> int:
        maxP = float('-inf')
        n = len(s)
        for mask in range(1 << n):
            sub = ""
            rest = ""
            for j in range(n):
                if mask & (1 << j):
                    sub += s[j]
                else:
                    rest += s[j]
            if len(sub) > 0 and len(rest) > 0:
                maxP = max(maxP, self.maxPalindrome(sub, 0, len(sub) - 1) * self.maxPalindrome(rest, 0, len(rest) - 1))
        return maxP