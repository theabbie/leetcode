class Solution:
    def maxPalindrome(self, s, i, j, cache):
        key = 1100 * i + j
        if key in cache:
            return cache[key]
        if i == j:
            cache[key] = 1
        elif s[i] == s[j] and i + 1 == j:
            cache[key] = 2
        elif s[i] == s[j]:
            cache[key] = self.maxPalindrome(s, i + 1, j - 1, cache) + 2
        else:
            cache[key] = max(self.maxPalindrome(s, i, j - 1, cache), self.maxPalindrome(s, i + 1, j, cache))
        return cache[key]
    
    def maxProduct(self, s: str) -> int:
        self.cache = {}
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
                maxP = max(maxP, self.maxPalindrome(sub, 0, len(sub) - 1, {}) * self.maxPalindrome(rest, 0, len(rest) - 1, {}))
        return maxP