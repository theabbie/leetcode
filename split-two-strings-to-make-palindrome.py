class Solution:
    def manachers(self, s):
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            if R > i:
                P[i] = min(R - i, P[2 * C - i])
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > R:
                C, R = i, i + P[i]
        return P
    
    def check(self, a, b):
        n = len(a)
        s = a + b
        pal = self.manachers(s)
        ispal = lambda x, y: pal[x + y + 2] >= y - x + 1
        maxmatch = 0
        i = 0
        j = 2 * n - 1
        while i < j and s[i] == s[j]:
            maxmatch += 1
            i += 1
            j -= 1
        for pref in range(n + 1):
            suff = n - pref
            if min(pref, suff) > maxmatch:
                continue
            diff = abs(pref - suff)
            if pref >= suff:
                if diff == 0 or ispal(pref - diff, pref - 1):
                    return True
            else:
                if ispal(2 * n - suff, 2 * n - suff + diff - 1):
                    return True
        return False
    
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.check(a, b) or self.check(b, a)