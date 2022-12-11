class Solution:
    def checkRecord(self, s: str) -> bool:
        n = len(s)
        a = 0
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and s[i] == s[i + 1]:
                ctr += 1
                i += 1
            if s[i] == 'L' and ctr >= 3:
                return False
            if s[i] == 'A':
                a += ctr
            i += 1
        return a < 2