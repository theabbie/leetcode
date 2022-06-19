class Solution:
    def longest(self, s, i, k):
        if i == 0:
            return 1 if int(s[i]) <= k else 0
        if (i, k) in self.cache:
            return self.cache[(i, k)]
        a = float('-inf')
        if k >= int(s[i]):
            a = 1 + self.longest(s, i - 1, (k - int(s[i])) // 2)
        b = self.longest(s, i - 1, k)
        res = max(a, b)
        self.cache[(i, k)] = res
        return res
    
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        mlen = 0
        self.cache = {}
        return self.longest(s, n - 1, k)