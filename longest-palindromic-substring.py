class Solution:
    def longestPalindrome(self, s: str) -> str:
        cache = {}
        def blackbox(i, j):
            if i < 0:
                return False
            if i >= j:
                return True
            key = n * i + j
            if key in cache:
                return cache[key]
            cache[key] = s[i] == s[j] and blackbox(i + 1, j - 1)
            return cache[key]
        n = len(s)
        pal = [0] * n
        pal[0] = 1
        res = (1, 0, 1)
        for i in range(1, n):
            pal[i] = pal[i - 1] + 2
            while not blackbox(i - pal[i] + 1, i):
                pal[i] -= 1
            res = max(res, (pal[i], i - pal[i] + 1, i + 1))
        return s[res[1]:res[2]]