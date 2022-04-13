class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            if (s[i].isupper() ^ s[i + 1].isupper()) and s[i].lower() == s[i + 1].lower():
                s = s[:i] + s[i + 2:]
                i = max(i - 1, 0)
            else:
                i += 1
        return s