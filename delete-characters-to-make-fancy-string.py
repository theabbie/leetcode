class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        i = 0
        op = ""
        while i < n:
            ctr = 1
            while i < n - 1 and s[i] == s[i + 1]:
                ctr += 1
                i += 1
            i += 1
            op += s[i - 1] * min(2, ctr)
        return op