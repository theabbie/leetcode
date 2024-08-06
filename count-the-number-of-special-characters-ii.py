class Solution:
    def numberOfSpecialChars(self, s: str) -> int:
        n = len(s)
        res = 0
        f = {}
        for i in range(n):
            if s[i].isupper() and s[i].lower() not in f:
                f[s[i].lower()] = i
        l = {}
        for i in range(n):
            if s[i].islower():
                l[s[i]] = i
        return len([el for el in l if el in f and l[el] < f[el]])