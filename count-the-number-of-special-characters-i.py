class Solution:
    def numberOfSpecialChars(self, s: str) -> int:
        n = len(s)
        res = 0
        f = set()
        for i in range(n):
            if s[i].isupper():
                f.add(s[i].lower())
        l = set()
        for i in range(n):
            if s[i].islower():
                l.add(s[i])
        return len(f & l)