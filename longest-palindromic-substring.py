class Solution:
    def strech(self, s, i, j, n):
        l = 0
        while i - l >= 0 and j + l < n and s[i - l] == s[j + l]:
            l += 1
        l -= 1
        return (i - l, j + l)
    
    def longestPalindrome(self, s) -> str:
        n = len(s)
        mx, my = 0, 0
        for i in range(n - 1):
            for a, b in [(i, i), (i, i + 1)]:
                x, y = self.strech(s, a, b, n)
                if y - x > my - mx:
                    mx, my = x, y
        return s[mx:my+1]