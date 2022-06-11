class Solution:
    def strongPasswordCheckerII(self, p: str) -> bool:
        n = len(p)
        if len(p) < 8:
            return False
        lc = 0
        uc = 0
        dg = 0
        sc = 0
        for i in range(n):
            if p[i].islower():
                lc += 1
            if p[i].isupper():
                uc += 1
            if p[i].isdigit():
                dg += 1
            if p[i] in "!@#$%^&*()-+":
                sc += 1
            if i < n - 1 and p[i] == p[i + 1]:
                return False
        return lc >= 1 and uc >= 1 and dg >= 1 and sc >= 1