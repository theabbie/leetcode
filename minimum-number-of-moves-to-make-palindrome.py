class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        f = {}
        l = {}
        for i in range(len(s)):
            if s[i] not in f:
                f[s[i]] = i
            l[s[i]] = i
        minmoves = (float('inf'), "z")
        for i in range(26):
            c = chr(ord('a') + i)
            if f.get(c, float('inf')) < l.get(c, float('-inf')):
                minmoves = min(minmoves, (f.get(c, float('inf')) + len(s) - 1 - l.get(c, float('-inf')), c))
        i = f[minmoves[1]]
        j = l[minmoves[1]]
        news = s[:i] + s[i+1:j] + s[j+1:]
        return minmoves[0] + self.minMovesToMakePalindrome(news)