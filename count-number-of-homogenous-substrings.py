class Solution:
    def countHomogenous(self, s: str) -> int:
        M = 10 ** 9 + 7
        n = len(s)
        res = 0
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and s[i] == s[i + 1]:
                i += 1
                ctr += 1
            i += 1
            res = (res + ctr * (ctr + 1) // 2) % M
        return res